# -*- coding: utf-8 -*-
import json
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import render_to_string

from common import create_from_form_post, create_from_form_edit, get_pair, asbtr_preview_csv, paginate, abstr_all
from ..forms import SeasonYearsOnly, MentorForm, UploadForm
from ..models.season import Season
from ..models.mentor import Mentor

def all(request):
    view_info = {
        'model': Mentor,
        'title': u'Ръководители',
        'table_template': 'mentors/_table.html',
    }

    urls = {
        'create': 'create_mentor',
        'edit': 'edit_mentor',
        'delete': 'delete_mentor',
        'preview': 'preview_mentors',
    }

    return abstr_all(request, urls, view_info)

def get_page(request, page_num):
    if(request.is_ajax()):
        page = paginate(page_num, Mentor)
        html = render_to_string('mentors/_table.html', {
            'objects': page,
            'urls': {
                'edit': 'edit_mentor',
                'delete': 'delete_mentor',
            },
        })

        return HttpResponse(html)

def edit(request, id):
    mentor = Mentor.objects.filter(id=id)
    if not id or not mentor.exists():
        return HttpResponseRedirect('/mentors/create')
    else: 
        context_data = {
            'title': u'Промени ръководител',
            'year': datetime.now().year,
            'id': mentor[0].id,
            'season_form': SeasonYearsOnly(),
        }

        return create_from_form_edit(request, MentorForm, 
                            'all_mentors', 
                            'edit.html',
                            context_data,
                            mentor[0])

def create(request):
    context_data = {
        'title': u'Създай ръководител',
        'year': datetime.now().year,
        'season_form': SeasonYearsOnly(),
    }

    return create_from_form_post(request, MentorForm, 
                            'all_mentors', 
                            'create.html',
                            context_data)

def delete(request, id):
    if(request.is_ajax()):
        if(request.method == 'DELETE'):
            try:
                mentor = Mentor.objects.get(id=id)
                mentor.soft_delete()
            except Mentor.DoesNotExist:
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
            Mentor.create_from_upload(objects)

    return HttpResponseRedirect(reverse('all_mentors'))

def preview_csv(request):
    view = {
        'title': 'Ръководители',
        'name': 'mentors',
        'model': Mentor,
    }

    choices = [get_pair('-' * 9, ''),
               get_pair('Фирма', 'firm'),
               get_pair('Име', 'fname'),
               get_pair('Презиме', 'mname'),
               get_pair('Фамилия', 'lname')]

    return asbtr_preview_csv(request, view, choices)