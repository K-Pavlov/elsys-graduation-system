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
from ..forms.student import StudentForm
from ..forms.file import UploadForm
from ..models.season import Season
from ..models.student import Student
from . import create_from_form_post, create_from_form_edit

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
            'upload_form': UploadForm(),
            'season_form': SeasonYearsOnly()
        })
    )

def edit(request, id):
    student = Student.objects.filter(id=id)
    if not id or not student.exists():
        return HttpResponseRedirect('/students/create')
    else: 
        context_data = {
            'title': u'Промени ученик',
            'year': datetime.now().year,
            'id': student[0].id,
            'season_form': SeasonYearsOnly()
        }
        return create_from_form_edit(request, StudentForm, 
                            'all_students', 
                            'edit.html', 
                            context_data,
                            student[0])

def create(request):
    context_data = {
            'title': u'Създай ученик',
            'year': datetime.now().year,
            'season_form': SeasonYearsOnly()
        }

    return create_from_form_post(request, StudentForm, 
                            'all_students', 
                            'create.html', 
                            context_data)

def delete(request, id):
    if request.is_ajax():
        student = Student.objects.filter(id=id)
        student.delete()

        return HttpResponse(json.dumps('Success'), content_type = "application/json")

    return HttpResponseNotFound()

def upload_csv(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            Student.from_csv(form.cleaned_data['file'])
    return HttpResponseRedirect(reverse('all_students'))

def generate_protocol(request):
    context = {
        'students': Student.objects.all()
    }
    return render_to_pdf('students/students_table.html', context)
   