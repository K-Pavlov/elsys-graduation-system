# -*- coding: utf-8 -*-
import json
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.template.loader import render_to_string

from division.forms import MentorForm
from division.models.mentor import Mentor
from shared.forms import SeasonYearsOnly, UploadForm, TeacherForm
from shared.models.season import Season
from common.views import get_pair, paginate
from common.views import abstr_all, abstr_delete, abstr_preview_csv, abstr_upload_data

def all(request):
    view_info = {
        'model': Mentor,
        'title': u'Ръководители',
        'table_template': 'mentors/_table.html',
    }

    urls = {
        'create': 'create_mentor',
        'edit': 'edit_mentor',
        'delete': 'delete_mentor',
        'preview': 'preview_mentors',
    }

    return abstr_all(request, urls, view_info)

def get_page(request, page_num):
    if(request.is_ajax()):
        page = paginate(page_num, Mentor)
        html = render_to_string('mentors/_table.html', {
            'objects': page,
            'urls': {
                'edit': 'edit_mentor',
                'delete': 'delete_mentor',
            },
        })

        return HttpResponse(html)

def edit(request, id):
    mentor = get_object_or_404(Mentor, pk=id)
    context_data = {
        'title': u'Променете ръководител',
        'year': datetime.now().year,
        'id': mentor.id,
        'season_form': SeasonYearsOnly(),
    }

    if(request.method == 'POST'):
        mentor_form = MentorForm(request.POST, instance=mentor)
        teacher_form = TeacherForm(request.POST, instance=mentor.teacher)
        if(mentor_form.is_valid() and teacher_form.is_valid()):
            mentor = mentor_form.save()
            teacher = teacher_form.save()
            return HttpResponseRedirect(reverse('all_mentors'))
    else:
        mentor_form = MentorForm(instance=mentor)
        teacher_form = TeacherForm(instance=mentor.teacher)

    context_data['mentor_form'] = mentor_form
    context_data['teacher_form'] = teacher_form

    return render(request,
        'mentors/edit.html',
        context_instance = RequestContext(request, context_data))

def create(request):
    context_data = {
        'title': u'Създайте ръководител',
        'year': datetime.now().year,
        'season_form': SeasonYearsOnly(),
    }

    if(request.method == 'POST'):
        mentor_form = MentorForm(request.POST)
        teacher_form = TeacherForm(request.POST)
        if(mentor_form.is_valid() and teacher_form.is_valid()):
            mentor = mentor_form.save(commit=False)
            teacher = teacher_form.save()
            mentor.teacher = teacher
            mentor.save()

            return HttpResponseRedirect(reverse('all_mentors'))
    else:
        mentor_form = MentorForm()
        teacher_form = TeacherForm()

    context_data['mentor_form'] = mentor_form
    context_data['teacher_form'] = teacher_form

    return render(request,
        'mentors/create.html',
        context_instance = RequestContext(request, context_data))

def delete(request, id):
    return abstr_delete(request, id, Mentor)

def upload_csv(request):
    return abstr_upload_data(request, Mentor, '/mentors')

def preview_csv(request):
    view = {
        'title': 'Ръководители',
        'name': 'mentors',
        'model': Mentor,
    }

    choices = [get_pair('-' * 9, ''),
               get_pair('Фирма', 'firm'),
               get_pair('Име', 'fname'),
               get_pair('Презиме', 'mname'),
               get_pair('Фамилия', 'lname')]

    return abstr_preview_csv(request, view, choices)