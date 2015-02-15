# -*- coding: utf-8 -*-
import json
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import render_to_string

from common import create_from_form_post, create_from_form_edit, paginate, abstr_all
from ..forms.season import SeasonYearsOnly
from ..forms.klass import SpecializationForm
from ..forms.file import UploadForm
from ..models.season import Season
from ..models.specialization import Specialization

def all(request):
    view_info = {
        'model': Specialization,
        'title': u'Специалности',
        'table_template': 'specializations/_table.html',
    }

    urls = {
        'create': 'create_specialization',
        'edit': 'edit_specialization',
        'delete': 'delete_specialization',
    }

    return abstr_all(request, urls, view_info)

def get_page(request, page_num):
    if(request.is_ajax()):
        page = paginate(page_num, Specialization)
        html = render_to_string('specializations/_table.html', {
            'objects': page,
            'urls': {
                'edit': 'edit_specialization',
                'delete': 'delete_specialization',
            },
        })

        return HttpResponse(html)

def edit(request, id):
    specialization = Specialization.objects.filter(id=id)
    if not id or not specialization.exists():
        return HttpResponseRedirect('/specializations/create')
    else: 
        context_data = {
            'title': u'Промени специалност',
            'year': datetime.now().year,
            'id': specialization[0].id,
            'season_form': SeasonYearsOnly(),
        }

        return create_from_form_edit(request, SpecializationForm, 
                            'all_specializations', 
                            'edit.html',
                            context_data,
                            specialization[0])

def create(request):
    context_data = {
            'title': u'Създай специалност',
            'year': datetime.now().year,
            'season_form': SeasonYearsOnly(),
        }

    return create_from_form_post(request, SpecializationForm, 
                            'all_specializations', 
                            'create.html',
                            context_data)

def delete(request, id):
    if request.is_ajax():
        if request.method == 'DELETE':
            try:
                specialization = Specialization.objects.get(id=id)
                specialization.soft_delete()
            except Specialization.DoesNotExist:
                return HttpResponseNotFound(json.dumps({
                                    error: 'Възникна проблем при изтриването на записа, моля опитайте отново.'
                                }), content_type = "application/json")

            return HttpResponse(json.dumps('Success'), content_type = "application/json")

    raise Http404