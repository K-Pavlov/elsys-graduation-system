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

from ..forms.season import SeasonYearsOnly
from ..common.pdf_renderer import render_to_pdf
from ..forms.teacher import TeacherForm
from ..forms.file import UploadForm
from ..models.season import Season
from ..models.teacher import Teacher
from . import create_from_form_post, create_from_form_edit

def all(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'teachers/all.html',
        context_instance = RequestContext(request,
        {
            'title': u'Учители',
            'year': datetime.now().year,
            'teachers': Teacher.objects.all(),
            'upload_form': UploadForm(),
            'season_form': SeasonYearsOnly()
        })
    )

def edit(request, id):
    teacher = Teacher.objects.filter(id=id)
    if not id or not teacher.exists():
        return HttpResponseRedirect('/teachers/create')
    else: 
        context_data = {
            'title': u'Промени учител',
            'year': datetime.now().year,
            'id': teacher[0].id,
            'season_form': SeasonYearsOnly()
        }
        return create_from_form_edit(request, TeacherForm, 
                            'all_teachers', 
                            'edit.html', 
                            context_data,
                            teacher[0])

def create(request):
    context_data = {
            'title': u'Създай учител',
            'year': datetime.now().year,
            'season_form': SeasonYearsOnly()
        }

    return create_from_form_post(request, TeacherForm, 
                            'all_teachers', 
                            'create.html', 
                            context_data)

def delete(request, id):
    if request.is_ajax():
        teacher = Teacher.objects.filter(id=id)
        teacher.delete()

        return HttpResponse(json.dumps('Success'), content_type = "application/json")

    return HttpResponseNotFound()

def upload_csv(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            Teacher.from_csv(form.cleaned_data['file'])
    return HttpResponseRedirect(reverse('all_teachers'))

def generate_protocol(request):
    context = {
        'teachers': Teacher.objects.all()
    }
    return render_to_pdf('teachers/teachers_table.html', context)
   