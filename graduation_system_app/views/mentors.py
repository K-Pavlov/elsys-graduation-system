# -*- coding: utf-8 -*-
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext

from ..forms.mentor_form import MentorForm
from ..models.mentor import Mentor
from . import create_from_form

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
    if not id or Mentor.objects.filter(id=id).exists():
        return HttpResponseRedirect('/mentors/create')
    else: 
        context_data = {
            'title': u'Промени ръководител',
            'year': datetime.now().year,
        }
        return create_from_form(request, MentorForm, 
                            'all_mentors', 
                            'mentors/edit.html', context_data)

def create(request):
    context_data = {
            'title': u'Създай ръководител',
            'year': datetime.now().year,
        }

    return create_from_form(request, MentorForm, 
                            'all_mentors', 
                            'mentors/create.html', context_data)

def delete(request, id):
    pass

