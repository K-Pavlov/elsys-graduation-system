# -*- coding: utf-8 -*-
import json
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import render_to_string

from common import create_from_form_post, create_from_form_edit, get_pair, asbtr_preview_csv, paginate, abstr_all
from ..forms import SeasonYearsOnly, RefereeForm, UploadForm, TeacherForm
from ..models.season import Season
from ..models.referee import Referee, Referal

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

    if request.method == 'POST':
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
    if request.is_ajax():
        if request.method == 'DELETE':
            try:
                referee = Referee.objects.get(id=id)
                referee.soft_delete()
            except Referee.DoesNotExist:
                return HttpResponseNotFound(json.dumps({
                                    error: 'Възникна проблем при изтриването на записа, моля опитайте отново.'
                                }), content_type = "application/json")

            return HttpResponse(json.dumps('Success'), content_type = "application/json")

    raise Http404

def upload_csv(request):
    if(request.is_ajax()):
        if(request.method == 'POST'):
            post_as_list = list(request.POST.iterlists())
            # Elements in the list are tuples 
            referee_tuple = post_as_list[0]

            # So we need need the first argument of the tuple
            # which holds our json data
            referee_data = referee_tuple[0]

            objects = json.loads(referee_data.encode('utf-8'))
            Referee.create_from_upload(objects)

            return HttpResponse(json.dumps({
                                    'redir': '/referees'
                                }))

    raise Http404

def upload_referal(request):
    form = UploadForm()
    if(request.method == 'POST'):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
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
                print('Err')

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
               get_pair('Имайл', 'email'),
               get_pair('Фирма', 'firm'),]

    return asbtr_preview_csv(request, view, choices)