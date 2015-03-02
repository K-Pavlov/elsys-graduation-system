# -*- coding: utf-8 -*-
import json
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import render_to_string

from common import create_from_form_post, create_from_form_edit, paginate, abstr_all
from ..common.pdf_renderer import render_to_pdf
from ..forms import TeacherForm, UploadForm, SeasonYearsOnly
from ..models.season import Season
from ..models.teacher import Teacher

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
    teacher = Teacher.objects.filter(id=id)
    if not id or not teacher.exists():
        return HttpResponseRedirect('/teachers/create')
    else: 
        context_data = {
            'title': u'Променете учител',
            'year': datetime.now().year,
            'id': teacher[0].id,
            'season_form': SeasonYearsOnly()
        }
        return create_from_form_edit(request, TeacherForm, 
                            'all_teachers', 
                            'edit.html', 
                            context_data,
                            teacher[0])

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
    if(request.is_ajax()):
        try:
            teacher = Teacher.objects.get(id=id)
            teacher.soft_delete()
        except Teacher.DoesNotExist:
            return HttpResponseNotFound(json.dumps({
                                    error: 'Възникна проблем при изтриването на записа, моля опитайте отново.'
                                }), content_type = "application/json")

        return HttpResponse(json.dumps('Success'), content_type = "application/json")

    raise Http404
   