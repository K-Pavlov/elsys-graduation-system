# -*- coding: utf-8 -*-
import json
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.template.loader import render_to_string

from division.forms import StudentForm
from division.models.student import Student
from shared.forms import SeasonYearsOnly, UploadForm
from shared.models.season import Season
from common.views import create_from_form_post, create_from_form_edit, get_pair, paginate
from common.views import abstr_all, abstr_delete, abstr_preview_csv, abstr_upload_data

def all(request):
    view_info = {
        'model': Student,
        'title': u'Ученици',
        'table_template': 'students/_table.html',
    }

    urls = {
        'create': 'create_student',
        'edit': 'edit_student',
        'delete': 'delete_student',
        'preview': 'preview_students',
    }

    return abstr_all(request, urls, view_info)

def get_page(request, page_num):
    if(request.is_ajax()):
        page = paginate(page_num, Student)
        html = render_to_string('students/_table.html', RequestContext(request, {
            'objects': page,
            'urls': {
                'edit': 'edit_student',
                'delete': 'delete_student',
            },
        }))

        return HttpResponse(html)

def edit(request, id):
    student = get_object_or_404(Student, pk=id)
    context_data = {
        'title': u'Променете ученик',
        'year': datetime.now().year,
        'id': student.id,
        'season_form': SeasonYearsOnly()
    }

    return create_from_form_edit(request, StudentForm, 
                        'all_students', 
                        'edit.html', 
                        context_data,
                        student)

def create(request):
    context_data = {
            'title': u'Създайте ученик',
            'year': datetime.now().year,
            'season_form': SeasonYearsOnly()
        }

    return create_from_form_post(request, StudentForm, 
                            'all_students', 
                            'create.html', 
                            context_data)

def delete(request, id):
    return abstr_delete(request, id, Student)

def upload_csv(request):
    return abstr_upload_data(request, Student, '/students')

def preview_csv(request):
    view = {
        'title': 'Ученици',
        'name': 'students',
        'model': Student,
    }

    choices = [get_pair('-' * 9, ''),
               get_pair('Име', 'fname'),
               get_pair('Презиме', 'mname'),
               get_pair('Фамилия', 'lname'), 
               get_pair('Паралелка', 'class-letter'),
               get_pair('Специалност', 'spec'),
               get_pair('Тема', 'topic'),
               get_pair('Име на ръководител', 'fname-mentor'),
               get_pair('Презиме на ръководител', 'mname-mentor'),
               get_pair('Фамилия на ръководител', 'lname-mentor'),
               get_pair('Фирма на ръководител', 'firm'),]

    return abstr_preview_csv(request, view, choices)