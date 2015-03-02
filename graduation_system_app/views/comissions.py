# -*- coding: utf-8 -*-
import json
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import render_to_string


from common import create_from_form_post, create_from_form_edit, get_pair, asbtr_preview_csv, paginate, abstr_all
from ..forms import SeasonYearsOnly, ComissionForm, UploadForm
from ..common.pdf_renderer import render_to_pdf
from ..models.season import Season
from ..models.comission import Comission

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
    if request.is_ajax():
        try:
            comission = Comission.objects.get(id=id)
            comission.soft_delete()
        except Comission.DoesNotExist:
            return HttpResponseNotFound(json.dumps({
                                    error: 'Възникна проблем при изтриването на записа, моля опитайте отново.'
                                }), content_type = "application/json")

        return HttpResponse(json.dumps('Success'), content_type = "application/json")

    raise Http404
   