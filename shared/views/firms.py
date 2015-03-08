# -*- coding: utf-8 -*-

import json
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import render_to_string

from shared.forms import SeasonYearsOnly, FirmForm
from shared.models.season import Season
from shared.models.firm import Firm
from views_common import create_from_form_post, create_from_form_edit, paginate, abstr_all

def all(request):
    view_info = {
        'model': Firm,
        'title': u'Фирми',
        'table_template': 'firms/_table.html',
    }

    urls = {
        'create': 'create_firm',
        'edit': 'edit_firm',
        'delete': 'delete_firm',
    }

    return abstr_all(request, urls, view_info)

def get_page(request, page_num):
    if(request.is_ajax()):
        page = paginate(page_num, Firm)
        html = render_to_string('firms/_table.html', {
            'objects': page,
            'urls': {
                'edit': 'edit_firm',
                'delete': 'delete_firm',
            },
        })

        return HttpResponse(html)

def edit(request, id):
    firm = Firm.objects.filter(id=id)
    if not id or not firm.exists():
        return HttpResponseRedirect('/firms/create')
    else: 
        context_data = {
            'title': u'Променете фирма',
            'year': datetime.now().year,
            'id': firm[0].id,
            'season_form': SeasonYearsOnly(),
        }

        return create_from_form_edit(request, FirmForm, 
                            'all_firms', 
                            'edit.html',
                            context_data,
                            firm[0])

def create(request):
    context_data = {
            'title': u'Създайте фирма',
            'year': datetime.now().year,
            'season_form': SeasonYearsOnly(),
        }

    return create_from_form_post(request, FirmForm, 
                            'all_firms', 
                            'create.html',
                            context_data)

def delete(request, id):
    if request.is_ajax():
        if request.method == 'DELETE':
            try:
                firm = Firm.objects.get(id=id)
                firm.soft_delete()
            except Firm.DoesNotExist:
                return HttpResponseNotFound(json.dumps({
                                    error: 'Възникна проблем при изтриването на записа, моля опитайте отново.'
                                }), content_type = "application/json")

            return HttpResponse(json.dumps('Success'), content_type = "application/json")

    raise Http404