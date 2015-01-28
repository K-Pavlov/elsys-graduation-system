# -*- coding: utf-8 -*-
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
from ..forms.klass import KlassForm
from ..forms.file import UploadForm
from ..models.season import Season
from ..models.klass import Klass
from . import create_from_form_post, create_from_form_edit

def all(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    current_season = Season.objects.get(is_active=True)
    return render(
        request,
        'klasses/all.html',
        context_instance = RequestContext(request,
        {
            'title': u'Класове',
            'season': current_season.year,
            'year': datetime.now().year,
            'klasses': Klass.objects.all(),
            'season_form': SeasonYearsOnly(),
        })
    )

def edit(request, id):
    klass = Klass.objects.filter(id=id)
    current_season = Season.objects.get(is_active=True)
    if not id or not klass.exists():
        return HttpResponseRedirect('/klasses/create')
    else: 
        context_data = {
            'title': u'Промени клас',
            'season': current_season.year,
            'year': datetime.now().year,
            'id': klass[0].id,
            'season_form': SeasonYearsOnly(),
        }
        print(klass[0])

        return create_from_form_edit(request, KlassForm, 
                            'all_klasses', 
                            'klasses/edit.html',
                            context_data,
                            klass[0])

def create(request):
    current_season = Season.objects.get(is_active=True)
    context_data = {
            'title': u'Създай клас',
            'season': current_season.year,
            'year': datetime.now().year,
            'season_form': SeasonYearsOnly(),
        }

    return create_from_form_post(request, KlassForm, 
                            'all_klasses', 
                            'klasses/create.html',
                            context_data)

def delete(request, id):
    if request.is_ajax():
        if request.method == 'DELETE':
            klass = Klass.objects.filter(id=id)
            klass.delete()

            return HttpResponse(json.dumps('Success'), content_type = "application/json")

    return HttpResponseNotFound(json.dumps({
                                    error: 'Възникна проблем при изтриването на записа, моля опитайте отново.'
                                }), content_type = "application/json")



