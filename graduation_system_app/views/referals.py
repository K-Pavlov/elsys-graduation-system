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
from ..forms.season import SeasonYearsOnly
from ..forms.referal import ReferalForm
from ..forms.file import UploadForm
from ..models.season import Season
from ..models.referee import Referal

def all(request):
    return render(
        request,
        'referals/all.html',
        context_instance = RequestContext(request,
        {
            'title': u'Рецензии',
            'year': datetime.now().year,
            'referals': Referal.objects.all(),
            'season_form': SeasonYearsOnly(),
        })
    )

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
        print(referal[0])

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
            referal = Referal.objects.filter(id=id)
            referal.delete()

            return HttpResponse(json.dumps('Success'), content_type = "application/json")

    return HttpResponseNotFound(json.dumps({
                                    error: 'Възникна проблем при изтриването на записа, моля опитайте отново.'
                                }), content_type = "application/json")

