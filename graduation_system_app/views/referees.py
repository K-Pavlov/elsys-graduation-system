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

from ..forms.referee import RefereeForm
from ..forms.file import UploadForm
from ..models.referee import Referee
from . import create_from_form_post, create_from_form_edit

def all(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'referees/all.html',
        context_instance = RequestContext(request,
        {
            'title': u'Рецензенти',
            'year': datetime.now().year,
            'referees': Referee.objects.all(),
            'upload_form': UploadForm(),
        })
    )

def edit(request, id):
    referee = Referee.objects.filter(id=id)
    if not id or not referee.exists():
        return HttpResponseRedirect('/referees/create')
    else: 
        context_data = {
            'title': u'Промени рецензент',
            'year': datetime.now().year,
            'id': referee[0].id
        }
        print(referee[0])

        return create_from_form_edit(request, RefereeForm, 
                            'all_referees', 
                            'referees/edit.html',
                            context_data,
                            referee[0])

def create(request):
    context_data = {
            'title': u'Създай рецензент',
            'year': datetime.now().year,
        }

    return create_from_form_post(request, RefereeForm, 
                            'all_referees', 
                            'referees/create.html',
                            context_data)

def delete(request, id):
    if request.is_ajax():
        if request.method == 'DELETE':
            referee = Referee.objects.filter(id=id)
            referee.delete()

            return HttpResponse(json.dumps('Success'), content_type = "application/json")

    return HttpResponseNotFound(json.dumps({
                                    error: 'Възникна проблем при изтриването на записа, моля опитайте отново.'
                                }), content_type = "application/json")

def upload_csv(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            Referee.from_csv(form.cleaned_data['file'])

    return HttpResponseRedirect(reverse('all_referees'))

