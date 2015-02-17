# -*- coding: utf-8 -*-
import json
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import render_to_string


from common import create_from_form_post, create_from_form_edit, paginate, abstr_all
from ..forms import SeasonForm, SeasonYearsOnly
from ..models.season import Season

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
    season = Season.objects.filter(id=id)
    if not id or not season.exists():
        return HttpResponseRedirect('/seasons/create')
    else: 
        context_data = {
            'title': u'Промени сезон',
            'year': datetime.now().year,
            'id': season[0].id,
            'season_form': SeasonYearsOnly(),
        }

        return create_from_form_edit(request, SeasonForm, 
                            'all_seasons', 
                            'edit.html',
                            context_data,
                            season[0])

def create(request):
    context_data = {
            'title': u'Създай сезон',
            'year': datetime.now().year,
            'season_form': SeasonYearsOnly(),
        }

    return create_from_form_post(request, SeasonForm, 
                            'all_seasons', 
                            'create.html',
                            context_data)

def delete(request, id):
    if request.is_ajax():
        if request.method == 'DELETE':
            try:
                season = Season.objects.get(id=id)
                season.soft_delete()
            except Season.DoesNotExist:
                return HttpResponseNotFound(json.dumps({
                                    error: 'Възникна проблем при изтриването на записа, моля опитайте отново.'
                                }), content_type = "application/json")

            return HttpResponse(json.dumps('Success'), content_type = "application/json")

    raise Http404

def change(request):
    if request.is_ajax():
        if request.method == 'POST':
            form = SeasonYearsOnly(request.POST)
            if form.is_valid():
                answer = form.cleaned_data['years']
                try:
                    print Season.objects.select_related()
                    season = Season.objects.get(year= answer)
                    season.is_active = True
                    season.save()
                except Season.DoesNotExist:
                    for season in Season.objects.all():
                        season.is_active = False
                        season.save()

            return HttpResponse(json.dumps('Success'), content_type = "application/json")

    raise Http404
