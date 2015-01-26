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

from ..forms.mentor import MentorForm
from ..forms.file import UploadForm
from ..models.mentor import Mentor
from . import create_from_form_post, create_from_form_edit

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
            'upload_form': UploadForm(),
        })
    )

def edit(request, id):
    mentor = Mentor.objects.filter(id=id)
    if not id or not mentor.exists():
        return HttpResponseRedirect('/mentors/create')
    else: 
        context_data = {
            'title': u'Промени ръководител',
            'year': datetime.now().year,
            'id': mentor[0].id
        }

        return create_from_form_edit(request, MentorForm, 
                            'all_mentors', 
                            'mentors/edit.html',
                            context_data,
                            mentor[0])

def create(request):
    context_data = {
            'title': u'Създай ръководител',
            'year': datetime.now().year,
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

    return HttpResponseRedirect(reverse('all_topics'))

