# -*- coding: utf-8 -*-
import json
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext

from common import create_from_form_post, create_from_form_edit
from ..forms.season import SeasonForm, SeasonYearsOnly
from ..models.season import Season

def all(request):
    return render(
        request,
        'seasons/all.html',
        context_instance = RequestContext(request,
        {
            'title': u'Сезони',
            'year': datetime.now().year,
            'seasons': Season.objects.all(),
            'season_form': SeasonYearsOnly(),
        })
    )

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

    return HttpResponseNotFound(json.dumps({
                                    error: 'Възникна проблем при изтриването на записа, моля опитайте отново.'
                                }), content_type = "application/json")

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

    return HttpResponseNotFound(json.dumps({
                                    error: 'Възникна проблем при изтриването на записа, моля опитайте отново.'
                                }), content_type = "application/json")
