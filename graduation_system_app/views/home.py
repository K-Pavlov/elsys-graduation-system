# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def index(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'index.html',
        context_instance = RequestContext(request,
        {
            'title': u'Система за дипломиране',
            'year': datetime.now().year,
        })
    )