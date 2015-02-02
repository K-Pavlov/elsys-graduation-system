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

from ..forms.season import SeasonYearsOnly
from ..forms.klass import SpecializationForm
from ..forms.file import UploadForm
from ..models.season import Season
from ..models.specialization import Specialization
from . import create_from_form_post, create_from_form_edit

def all(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    #
    return render(
        request,
        'specializations/all.html',
        context_instance = RequestContext(request,
        {
            'title': u'Специалности',
            'year': datetime.now().year,
            'specializations': Specialization.objects.all(),
            'season_form': SeasonYearsOnly(),
        })
    )

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
            specialization = Specialization.objects.filter(id=id)
            specialization.delete()

            return HttpResponse(json.dumps('Success'), content_type = "application/json")

    return HttpResponseNotFound(json.dumps({
                                    error: 'Възникна проблем при изтриването на записа, моля опитайте отново.'
                                }), content_type = "application/json")