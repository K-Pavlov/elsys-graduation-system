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

from ..forms.season import SeasonForm
from ..models.season import Season
from . import create_from_form_post, create_from_form_edit

def all(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'seasons/all.html',
        context_instance = RequestContext(request,
        {
            'title': u'Сезони',
            'year': datetime.now().year,
            'seasons': Season.objects.all(),
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
            'id': mentor[0].id
        }

        return create_from_form_edit(request, SeasonForm, 
                            'all_seasons', 
                            'seasons/edit.html',
                            context_data,
                            season[0])

def create(request):
    context_data = {
            'title': u'Създай сезон',
            'year': datetime.now().year,
        }

    return create_from_form_post(request, SeasonForm, 
                            'all_seasons', 
                            'seasons/create.html',
                            context_data)

def delete(request, id):
    if request.is_ajax():
        if request.method == 'DELETE':
            season = Season.objects.filter(id=id)
            season.delete()

            return HttpResponse(json.dumps('Success'), content_type = "application/json")

    return HttpResponseNotFound(json.dumps({
                                    error: 'Възникна проблем при изтриването на записа, моля опитайте отново.'
                                }), content_type = "application/json")

def upload_csv(request):
    if request.is_ajax():
        if request.method == 'POST':
            file = request.FILES['file']
            if file:
                create_from_csv(file)
                return HttpResponse(json.dumps('Success'), content_type = "application/json")

    return HttpResponseNotFound(json.dumps({
                                    error: 'Възникна проблем при качването на файла, моля опитайте отново.'
                                }), content_type = "application/json")

def create_from_csv(csv_file):
    pass




