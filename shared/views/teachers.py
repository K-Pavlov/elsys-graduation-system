# -*- coding: utf-8 -*-
import json
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.template.loader import render_to_string

from shared.forms import SeasonYearsOnly, TeacherForm
from shared.models.season import Season
from shared.models.teacher import Teacher
from common.views import create_from_form_post, create_from_form_edit, paginate, abstr_all, abstr_delete

def all(request):
    view_info = {
        'model': Teacher,
        'title': u'Учители',
        'table_template': 'teachers/_table.html',
    }

    urls = {
        'create': 'create_teacher',
        'edit': 'edit_teacher',
        'delete': 'delete_teacher',
    }

    return abstr_all(request, urls, view_info)

def get_page(request, page_num):
    if(request.is_ajax()):
        page = paginate(page_num, Teacher)
        html = render_to_string('teachers/_table.html', {
            'objects': page,
            'urls': {
                'edit': 'edit_teacher',
                'delete': 'delete_teacher',
            },
        })

        return HttpResponse(html)

def edit(request, id):
    teacher = get_object_or_404(Teacher, pk=id)
    context_data = {
        'title': u'Променете учител',
        'year': datetime.now().year,
        'id': teacher.id,
        'season_form': SeasonYearsOnly()
    }

    return create_from_form_edit(request, TeacherForm, 
                        'all_teachers', 
                        'edit.html', 
                        context_data,
                        teacher)

def create(request):
    context_data = {
            'title': u'Създайте учител',
            'year': datetime.now().year,
            'season_form': SeasonYearsOnly()
        }

    return create_from_form_post(request, TeacherForm, 
                            'all_teachers', 
                            'create.html', 
                            context_data)

def delete(request, id):
    return abstr_delete(request, id, Teacher)   