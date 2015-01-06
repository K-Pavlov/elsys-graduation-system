# -*- coding: utf-8 -*-
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext

from ..forms.topic import TopicForm
from ..models.topic import Topic
from . import create_from_form

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
        })
    )

def edit(request, id):
    if not id or Mentor.objects.filter(id=id).exists():
        return HttpResponseRedirect('/topics/create')
    else: 
        context_data = {
            'title': u'Промени тема',
            'year': datetime.now().year,
        }
        return create_from_form(request, TopicForm, 
                            'all_mentors', 
                            'topics/edit.html', context_data)

def create(request):
    context_data = {
            'title': u'Създай тема',
            'year': datetime.now().year,
        }

    return create_from_form(request, TopicForm, 
                            'all_topics', 
                            'topics/create.html', context_data)

def delete(request, id):
    pass