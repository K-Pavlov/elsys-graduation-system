# -*- coding: utf-8 -*-
import json
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import render_to_string

from reviewing.forms import RefereeForm
from reviewing.models import Referee, Referal
from shared.forms import SeasonYearsOnly, UploadForm, TeacherForm
from shared.models.season import Season
from common.views import get_pair, paginate
from common.views import abstr_all, abstr_delete, abstr_preview_csv, abstr_upload_data

def all(request):
    view_info = {
        'model': Referee,
        'title': u'Рецензенти',
        'table_template': 'referees/_table.html',
    }

    urls = {
        'create': 'create_referee',
        'edit': 'edit_referee',
        'delete': 'delete_referee',
        'preview': 'preview_referees',
    }

    return abstr_all(request, urls, view_info)

def get_page(request, page_num):
    if(request.is_ajax()):
        page = paginate(page_num, Referee)
        html = render_to_string('referees/_table.html', {
            'objects': page,
            'urls': {
                'edit': 'edit_referee',
                'delete': 'delete_referee',
            },
        })

        return HttpResponse(html)

def edit(request, id):
    referee = Referee.objects.filter(id=id)
    if(not id or not referee.exists()):
        return HttpResponseRedirect('/referees/create')
    else: 
        context_data = {
            'title': u'Променете ръководител',
            'year': datetime.now().year,
            'id': referee[0].id,
            'season_form': SeasonYearsOnly(),
        }

    referee = referee[0]
    if(request.method == 'POST'):
        referee_form = RefereeForm(request.POST, instance=referee)
        teacher_form = TeacherForm(request.POST, instance=referee.teacher)
        if(referee_form.is_valid() and teacher_form.is_valid()):
            referee = referee_form.save()
            teacher = teacher_form.save()
            return HttpResponseRedirect(reverse('all_referees'))
    else:
        referee_form = RefereeForm(instance=referee)
        teacher_form = TeacherForm(instance=referee.teacher)

    context_data['referee_form'] = referee_form
    context_data['teacher_form'] = teacher_form
    return render(request,
        'referees/edit.html',
        context_instance = RequestContext(request, context_data))

def create(request):
    context_data = {
        'title': u'Създайте рецензент',
        'year': datetime.now().year,
        'season_form': SeasonYearsOnly(),
    }

    if(request.method == 'POST'):
        referee_form = RefereeForm(request.POST)
        teacher_form = TeacherForm(request.POST)
        if(referee_form.is_valid() and teacher_form.is_valid()):
            referee = referee_form.save(commit=False)
            teacher = teacher_form.save()
            referee.teacher = teacher
            referee.save()

            return HttpResponseRedirect(reverse('all_referees'))
    else:
        referee_form = RefereeForm()
        teacher_form = TeacherForm()

    context_data['referee_form'] = referee_form
    context_data['teacher_form'] = teacher_form

    return render(request,
        'referees/create.html',
        context_instance = RequestContext(request, context_data))

def delete(request, id):
    return abstr_delete(request, id, Referee)

def upload_csv(request):
    return abstr_upload_data(request, Referee, '/referees')

def upload_referal(request):
    form = UploadForm()
    if(request.method == 'POST'):
        form = UploadForm(request.POST, request.FILES)
        if(form.is_valid()):
            email = request.user.email
            try:
                referee = Referee.objects.get(email=email)
                try:
                    referal = Referal.objects.get(referee=referee)
                except Referal.DoesNotExist:
                    referal = Referal()
                    referal.referee = referee

                referal.file = form.cleaned_data['file']
                referal.save()
                form = UploadForm()
            except Referee.DoesNotExist:
                return HttpResponseServerError(request)

    return render(
        request,
        'referees/upload_referal.html',
        context_instance = RequestContext(request,
        {
            'title': u'Качване на рецензия',
            'year': datetime.now().year,
            'upload_form': form,
        })
    )

def preview_csv(request):
    view = {
        'title': 'Рецензенти',
        'name': 'referees',
        'model': Referee,
    }

    choices = [get_pair('-' * 9, ''),
               get_pair('Име', 'fname'),
               get_pair('Презиме', 'mname'),
               get_pair('Фамилия', 'lname'),
               get_pair('Фирма', 'firm'),
               get_pair('Имейл', 'email'),]

    return abstr_preview_csv(request, view, choices)