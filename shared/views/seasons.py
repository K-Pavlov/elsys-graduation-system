# -*- coding: utf-8 -*-
import json
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.template.loader import render_to_string

from shared.forms import SeasonForm, SeasonYearsOnly
from shared.models.season import Season
from common.views import create_from_form_post, create_from_form_edit, paginate, abstr_all, abstr_delete

def all(request):
    view_info = {
        'model': Season,
        'title': u'Сезони',
        'table_template': 'seasons/_table.html',
    }

    urls = {
        'create': 'create_season',
        'edit': 'edit_season',
        'delete': 'delete_season',
    }

    return abstr_all(request, urls, view_info)

def get_page(request, page_num):
    if(request.is_ajax()):
        page = paginate(page_num, Season)
        html = render_to_string('seasons/_table.html', {
            'objects': page,
            'urls': {
                'edit': 'edit_season',
                'delete': 'delete_season',
            },
        })

        return HttpResponse(html)

def edit(request, id):
    season = get_object_or_404(Season, pk=id)
    context_data = {
        'title': u'Променете сезон',
        'year': datetime.now().year,
        'id': season.id,
        'season_form': SeasonYearsOnly(),
    }

    return create_from_form_edit(request, SeasonForm, 
                        'all_seasons', 
                        'edit.html',
                        context_data,
                        season)

def create(request):
    context_data = {
            'title': u'Създайте сезон',
            'year': datetime.now().year,
            'season_form': SeasonYearsOnly(),
        }

    return create_from_form_post(request, SeasonForm, 
                            'all_seasons', 
                            'create.html',
                            context_data)

def delete(request, id):
    return abstr_delete(request, id, Season)

def change(request):
    if(request.is_ajax()):
        if(request.method == 'POST'):
            form = SeasonYearsOnly(request.POST)
            if(form.is_valid()):
                answer = form.cleaned_data['years']
                try:
                    season = Season.objects.get(year= answer)
                    season.is_active = True
                    season.save()
                except Season.DoesNotExist:
                    for season in Season.objects.all():
                        season.is_active = False
                        season.save()

            return HttpResponse(json.dumps('Success'), content_type = "application/json")

    raise Http404