# -*- coding: utf-8 -*-
import json
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import render_to_string

from common import create_from_form_post, create_from_form_edit, get_pair, asbtr_preview_csv, paginate, abstr_all
from ..common.pdf_renderer import render_to_pdf
from ..forms import StudentForm, UploadForm, SeasonYearsOnly
from ..models.season import Season
from ..models.student import Student

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
            'title': u'Промени ученик',
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
            'title': u'Създай ученик',
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
            stuff = list(request.POST.iterlists())
            objects = json.loads(stuff[0][0].encode('utf-8'))
            Student.create_from_upload(objects)

    return HttpResponseRedirect(reverse('all_mentors'))

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

def generate_protocol(request):
    context = {
        'students': Student.objects.all()
    }
    return render_to_pdf('students/students_table.html', context)