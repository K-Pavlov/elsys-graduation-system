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
from ..common.pdf_renderer import render_to_pdf
from ..forms.comission import ComissionForm
from ..forms.file import UploadForm
from ..models.season import Season
from ..models.comission import Comission
from . import create_from_form_post, create_from_form_edit

def all(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'comissions/all.html',
        context_instance = RequestContext(request,
        {
            'title': u'Ученици',
            'year': datetime.now().year,
            'comissions': Comission.objects.all(),
            'upload_form': UploadForm(),
            'season_form': SeasonYearsOnly()
        })
    )

def edit(request, id):
    comission = Comission.objects.filter(id=id)
    if not id or not comission.exists():
        return HttpResponseRedirect('/comissions/create')
    else: 
        context_data = {
            'title': u'Промени ученик',
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
            'title': u'Създай ученик',
            'year': datetime.now().year,
            'season_form': SeasonYearsOnly()
        }

    return create_from_form_post(request, ComissionForm, 
                            'all_comissions', 
                            'comissions/create.html', 
                            context_data)

def delete(request, id):
    if request.is_ajax():
        comission = Comission.objects.filter(id=id)
        comission.delete()

        return HttpResponse(json.dumps('Success'), content_type = "application/json")

    return HttpResponseNotFound()

def upload_csv(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            Comission.from_csv(form.cleaned_data['file'])
    return HttpResponseRedirect(reverse('all_comissions'))

def generate_protocol(request):
    context = {
        'comissions': Comission.objects.all()
    }
    return render_to_pdf('comissions/comissions_table.html', context)
   