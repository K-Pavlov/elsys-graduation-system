# -*- coding: utf-8 -*-
from datetime import datetime

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext

from graduation_system_app.models.student import Student

def all(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'students/all.html',
        context_instance = RequestContext(request,
        {
            'title': u'Ученици',
            'year': datetime.now().year,
            'students': Student.objects.all(),
        })
    )