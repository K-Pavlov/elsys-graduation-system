# -*- coding: utf-8 -*-

import json
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.template.loader import render_to_string

from reviewing.forms import ReferalForm
from reviewing.models import Referal
from shared.forms import SeasonYearsOnly, UploadForm
from shared.models.season import Season
from common.views import create_from_form_post, create_from_form_edit, paginate, abstr_all, abstr_delete

def all(request):
    view_info = {
        'model': Referal,
        'title': u'Рецензии',
        'table_template': 'referals/_table.html',
    }

    urls = {
        'create': 'create_referal',
        'edit': 'edit_referal',
        'delete': 'delete_referal',
    }

    return abstr_all(request, urls, view_info)

def get_page(request, page_num):
    if(request.is_ajax()):
        page = paginate(page_num, Referal)
        html = render_to_string('referals/_table.html', {
            'objects': page,
            'urls': {
                'edit': 'edit_referal',
                'delete': 'delete_referal',
            },
        })

        return HttpResponse(html)

def edit(request, id):
    referal = get_object_or_404(Referal, pk=id)
    context_data = {
        'title': u'Променете рецензия',
        'year': datetime.now().year,
        'id': referal.id,
        'season_form': SeasonYearsOnly(),
    }

    return create_from_form_edit(request, ReferalForm, 
                        'all_referals', 
                        'edit.html',
                        context_data,
                        referal)

def create(request):
    context_data = {
            'title': u'Създайте рецензия',
            'year': datetime.now().year,
            'season_form': SeasonYearsOnly(),
        }

    return create_from_form_post(request, ReferalForm, 
                            'all_referals', 
                            'create.html',
                            context_data)

def delete(request, id):
    return abstr_delete(request, id, Referal)