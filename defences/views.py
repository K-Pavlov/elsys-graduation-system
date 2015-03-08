# -*- coding: utf-8 -*-
import json
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils import timezone

from forms import ComissionForm
from models import Comission
from pdf_renderer import render_to_pdf
from division.models.student import Student
from shared.forms import SeasonYearsOnly, UploadForm
from shared.models.season import Season
from common.views import create_from_form_post, create_from_form_edit, paginate, abstr_all, abstr_delete

# Comissions
def all(request):
    view_info = {
        'model': Comission,
        'title': u'Комисии',
        'table_template': 'comissions/_table.html',
    }

    urls = {
        'create': 'create_comission',
        'edit': 'edit_comission',
        'delete': 'delete_comission',
    }

    return abstr_all(request, urls, view_info)

def get_page(request, page_num):
    if(request.is_ajax()):
        page = paginate(page_num, Comission)
        html = render_to_string('comissions/_table.html', {
            'objects': page,
            'urls': {
                'edit': 'edit_comission',
                'delete': 'delete_comission',
            },
        })

        return HttpResponse(html)

def edit(request, id):
    comission = Comission.objects.filter(id=id)
    if not id or not comission.exists():
        return HttpResponseRedirect('/comissions/create')
    else: 
        context_data = {
            'title': u'Променете комисия',
            'year': datetime.now().year,
            'id': comission[0].id,
            'season_form': SeasonYearsOnly()
        }
        return create_from_form_edit(request, ComissionForm, 
                            'all_comissions', 
                            'comissions/edit.html', 
                            context_data,
                            comission[0])

def create(request):
    context_data = {
            'title': u'Създайте комисия',
            'year': datetime.now().year,
            'season_form': SeasonYearsOnly()
        }

    return create_from_form_post(request, ComissionForm, 
                            'all_comissions', 
                            'comissions/create.html', 
                            context_data)

def delete(request, id):
    return abstr_delete(request, id, Comission)

# Protocols
def all_students(request):
    year = ''
    try:
        year = Season.objects.get(is_active=True).year.split('/')[1]
    except Season.DoesNotExist:
        pass

    context = {
        'students': Student.objects.all(),
        'year': year,
    }
    return render_to_pdf('protocols/all-students.html', context)

def comission_with_students(request, id):
    context = get_ctx_comission(id)

    return render_to_pdf('protocols/comission-students.html', context)

def comission_students_indepth(request, id):
    context = get_ctx_comission(id)

    return render_to_pdf('protocols/comission-students-indepth.html', context)

#Not view
def get_ctx_comission(id):
    try:
        comission = Comission.objects.get(id=id)
    except Comission.DoesNotExist:
        raise Http404

    print comission.start_time

    start_time = timezone.localtime(comission.start_time)

    date = ''
    time = ''
    if(start_time):
        date = start_time.date()
        hour = str(start_time.hour)
        minute = str(start_time.minute)

        if(len(hour) == 1):
            hour = '0' + hour

        if(len(minute) == 1):
            minute = '0' + minute

        time = hour + ':' + minute

    return {
        'comission': comission,
        'date': date,
        'time': time,
    }