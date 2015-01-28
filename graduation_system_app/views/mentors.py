# -*- coding: utf-8 -*-
import json
from pprint import pprint
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext

from ..forms.season import SeasonYearsOnly
from ..forms.mentor import MentorForm
from ..forms.file import UploadForm
from ..models.season import Season
from ..models.mentor import Mentor
from . import create_from_form_post, create_from_form_edit

def all(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    #pprint(Mentor.objects.all())
    current_season = Season.objects.get(is_active=True)
    return render(
        request,
        'mentors/all.html',
        context_instance = RequestContext(request,
        {
            'title': u'Ръководители',
            'season': current_season.year,
            'year': datetime.now().year,
            'mentors': Mentor.objects.all(),
            'upload_form': UploadForm(),
            'season_form': SeasonYearsOnly(),
        })
    )

def edit(request, id):
    current_season = Season.objects.get(is_active=True)
    mentor = Mentor.objects.filter(id=id)
    if not id or not mentor.exists():
        return HttpResponseRedirect('/mentors/create')
    else: 
        context_data = {
            'title': u'Промени ръководител',
            'season': current_season.year,
            'year': datetime.now().year,
            'id': mentor[0].id,
            'season_form': SeasonYearsOnly(),
        }

        return create_from_form_edit(request, MentorForm, 
                            'all_mentors', 
                            'mentors/edit.html',
                            context_data,
                            mentor[0])

def create(request):
    current_season = Season.objects.get(is_active=True)
    context_data = {
            'title': u'Създай ръководител',
            'season': current_season.year,
            'year': datetime.now().year,
            'season_form': SeasonYearsOnly(),
        }

    return create_from_form_post(request, MentorForm, 
                            'all_mentors', 
                            'mentors/create.html',
                            context_data)

def delete(request, id):
    if request.is_ajax():
        if request.method == 'DELETE':
            mentor = Mentor.objects.filter(id=id)
            mentor.delete()

            return HttpResponse(json.dumps('Success'), content_type = "application/json")

    return HttpResponseNotFound(json.dumps({
                                    error: 'Възникна проблем при изтриването на записа, моля опитайте отново.'
                                }), content_type = "application/json")

def upload_csv(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            Mentor.from_csv(form.cleaned_data['file'])

    return HttpResponseRedirect(reverse('all_mentors'))

