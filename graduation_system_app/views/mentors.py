# -*- coding: utf-8 -*-
from datetime import datetime

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from graduation_system_app.models.mentor import Mentor

def all(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'mentors/all.html',
        context_instance = RequestContext(request,
        {
            'title': u'Ръководители',
            'year': datetime.now().year,
            'mentors': Mentor.objects.all(),
        })
    )

def edit(request, id):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()

    return render(
        request,
        'mentors/edit.html',
        context_instance = RequestContext(request,
        {
            'title': u'Ръководители',
            'year': datetime.now().year,
            'form': form
        })
    )

def create(request):
    pass

def delete(request, id):
    pass

