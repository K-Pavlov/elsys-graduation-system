# -*- coding: utf-8 -*-

import json
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import render_to_string

from common import create_from_form_post, create_from_form_edit, paginate, abstr_all
from ..forms.season import SeasonYearsOnly
from ..forms.referal import ReferalForm
from ..forms.file import UploadForm
from ..models.season import Season
from ..models.referee import Referal

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
    referal = Referal.objects.filter(id=id)
    if not id or not referal.exists():
        return HttpResponseRedirect('/referals/create')
    else: 
        context_data = {
            'title': u'Променете рецензия',
            'year': datetime.now().year,
            'id': referal[0].id,
            'season_form': SeasonYearsOnly(),
        }

        return create_from_form_edit(request, ReferalForm, 
                            'all_referals', 
                            'edit.html',
                            context_data,
                            referal[0])

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
    if request.is_ajax():
        if request.method == 'DELETE':
            try:
                referal = Referal.objects.get(id=id)
                referal.soft_delete()
            except Referal.DoesNotExist:
                return HttpResponseNotFound(json.dumps({
                                    error: 'Възникна проблем при изтриването на записа, моля опитайте отново.'
                                }), content_type = "application/json")

            return HttpResponse(json.dumps('Success'), content_type = "application/json")

    raise Http404