# -*- coding: utf-8 -*-
import json
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import render_to_string

from common import create_from_form_post, create_from_form_edit, get_pair, asbtr_preview_csv, paginate, abstr_all
from ..forms import SeasonYearsOnly, RefereeForm, UploadForm
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
    if not id or not referee.exists():
        return HttpResponseRedirect('/referees/create')
    else: 
        context_data = {
            'title': u'Промени рецензент',
            'year': datetime.now().year,
            'id': referee[0].id,
            'season_form': SeasonYearsOnly()
        }

        return create_from_form_edit(request, RefereeForm, 
                            'all_referees', 
                            'edit.html',
                            context_data,
                            referee[0])

def create(request):
    context_data = {
            'title': u'Създай рецензент',
            'year': datetime.now().year,
            'season_form': SeasonYearsOnly(),
        }

    return create_from_form_post(request, RefereeForm, 
                            'all_referees', 
                            'create.html',
                            context_data)

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
            stuff = list(request.POST.iterlists())
            objects = json.loads(stuff[0][0].encode('utf-8'))
            Referee.create_from_upload(objects)

    return HttpResponseRedirect(reverse('all_mentors'))

def upload_referal(request):
    form = UploadForm()
    if(request.method == 'POST'):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            email = request.user.email
            try:
                referee = Referee.objects.get(email=email)
                referal = Referal()
                referal.referee = referee
                print('Not err')
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