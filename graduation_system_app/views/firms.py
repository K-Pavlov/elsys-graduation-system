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
from ..forms.firm import FirmForm
from ..forms.file import UploadForm
from ..models.season import Season
from ..models.firm import Firm

def all(request):
    return render(
        request,
        'firms/all.html',
        context_instance = RequestContext(request,
        {
            'title': u'Фирми',
            'year': datetime.now().year,
            'firms': Firm.objects.all(),
            'season_form': SeasonYearsOnly(),
        })
    )

def edit(request, id):
    firm = Firm.objects.filter(id=id)
    if not id or not firm.exists():
        return HttpResponseRedirect('/firms/create')
    else: 
        context_data = {
            'title': u'Промени фирма',
            'year': datetime.now().year,
            'id': firm[0].id,
            'season_form': SeasonYearsOnly(),
        }
        print(firm[0])

        return create_from_form_edit(request, FirmForm, 
                            'all_firms', 
                            'edit.html',
                            context_data,
                            firm[0])

def create(request):
    context_data = {
            'title': u'Създай фирма',
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
            firm = Firm.objects.filter(id=id)
            firm.delete()

            return HttpResponse(json.dumps('Success'), content_type = "application/json")

    return HttpResponseNotFound(json.dumps({
                                    error: 'Възникна проблем при изтриването на записа, моля опитайте отново.'
                                }), content_type = "application/json")