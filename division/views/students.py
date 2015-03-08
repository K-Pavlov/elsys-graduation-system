# -*- coding: utf-8 -*-
import json
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import render_to_string

from division.forms import StudentForm
from division.models.student import Student
from shared.forms import SeasonYearsOnly, UploadForm
from shared.models.season import Season
from common.views import create_from_form_post, create_from_form_edit, get_pair, asbtr_preview_csv, paginate, abstr_all

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
    student = Student.objects.filter(id=id)
    if not id or not student.exists():
        return HttpResponseRedirect('/students/create')
    else: 
        context_data = {
            'title': u'Променете ученик',
            'year': datetime.now().year,
            'id': student[0].id,
            'season_form': SeasonYearsOnly()
        }
        return create_from_form_edit(request, StudentForm, 
                            'all_students', 
                            'edit.html', 
                            context_data,
                            student[0])

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
    if request.is_ajax():
        try:
            student = Student.objects.get(id=id)
            student.soft_delete()
        except Student.DoesNotExist:
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
            student_tuple = post_as_list[0]

            # So we need need the first argument of the tuple
            # which holds our json data
            student_data = student_tuple[0]

            objects = json.loads(student_data.encode('utf-8'))
            Student.create_from_upload(objects)
            return HttpResponse(json.dumps({
                                    'redir': '/students'
                                }))

    raise Http404

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

    return asbtr_preview_csv(request, view, choices)