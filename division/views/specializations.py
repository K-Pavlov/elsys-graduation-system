# -*- coding: utf-8 -*-
import json
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.template.loader import render_to_string

from division.forms import SpecializationForm
from division.models.specialization import Specialization
from shared.forms import SeasonYearsOnly, UploadForm
from shared.models.season import Season
from common.views import create_from_form_post, create_from_form_edit, paginate, abstr_all, abstr_delete

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
    specialization = get_object_or_404(Specialization, pk=id)
    context_data = {
        'title': u'Променете специалност',
        'year': datetime.now().year,
        'id': specialization.id,
        'season_form': SeasonYearsOnly(),
    }

    return create_from_form_edit(request, SpecializationForm, 
                        'all_specializations', 
                        'edit.html',
                        context_data,
                        specialization)

def create(request):
    context_data = {
            'title': u'Създайте специалност',
            'year': datetime.now().year,
            'season_form': SeasonYearsOnly(),
        }

    return create_from_form_post(request, SpecializationForm, 
                            'all_specializations', 
                            'create.html',
                            context_data)

def delete(request, id):
    return abstr_delete(request, id, Specialization)