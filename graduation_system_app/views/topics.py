# -*- coding: utf-8 -*-
from datetime import datetime

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext

from graduation_system_app.models.topic import Topic

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
            'topics': Topic.objects.all()
        })
    )