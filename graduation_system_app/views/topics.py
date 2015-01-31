# -*- coding: utf-8 -*-
import json
import csv
from datetime import datetime
 
from django.core.urlresolvers import reverse
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
 
from ..forms.season import SeasonYearsOnly
from ..forms.topic import TopicForm
from ..forms.file import UploadForm
from ..models.season import Season
from ..models.topic import Topic
from . import create_from_form_post, create_from_form_edit
 
def all(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'topics/all.html',
        context_instance = RequestContext(request,
        {
            'title': u'Теми',
            'year': datetime.now().year,
            'topics': Topic.objects.all(),
            'upload_form': UploadForm(),
            'season_form': SeasonYearsOnly()
        })
    )
 
def edit(request, id):
    topic = Topic.objects.filter(id=id)
    if not id or not topic.exists():
        return HttpResponseRedirect('/topics/create')
    else:
        context_data = {
            'title': u'Промени тема',
            'year': datetime.now().year,
            'id': topic[0].id,
            'season_form': SeasonYearsOnly()
        }
        return create_from_form_edit(request, TopicForm,
                            'all_topics',
                            'topics/edit.html',
                            context_data,
                            topic[0])
 
def create(request):

    context_data = {
            'title': u'Създай тема',
            'year': datetime.now().year,
            'season_form': SeasonYearsOnly(),
        }
 
    return create_from_form_post(request, TopicForm,
                            'all_topics',
                            'topics/create.html',
                            context_data)
 
def delete(request, id):
    if request.is_ajax():
        topic = Topic.objects.filter(id=id)
        topic.delete()
 
        return HttpResponse(json.dumps('Success'), content_type = "application/json")
 
    return HttpResponseNotFound(json.dumps({
                                    error: 'Възникна проблем при изтриването на записа, моля опитайте отново.'
                                }), content_type = "application/json")
 
def upload_csv(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            Topic.from_csv(form.cleaned_data['file'])
    return HttpResponseRedirect(reverse('all_topics'))