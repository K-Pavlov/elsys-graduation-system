# -*- coding: utf-8 -*-
import json
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import render_to_string

from common import create_from_form_post, create_from_form_edit, get_pair, asbtr_preview_csv, paginate, abstr_all
from ..forms import SeasonYearsOnly, MentorForm, UploadForm, TeacherForm
from ..models.season import Season
from ..models.mentor import Mentor

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
    mentor = Mentor.objects.filter(id=id)
    if(not id or not mentor.exists()):
        return HttpResponseRedirect('/mentors/create')
    else: 
        context_data = {
            'title': u'Променете ръководител',
            'year': datetime.now().year,
            'id': mentor[0].id,
            'season_form': SeasonYearsOnly(),
        }

    mentor = mentor[0]
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

    if request.method == 'POST':
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
    if(request.is_ajax()):
        if(request.method == 'DELETE'):
            try:
                mentor = Mentor.objects.get(id=id)
                mentor.soft_delete()
            except Mentor.DoesNotExist:
                return HttpResponseNotFound(json.dumps({
                                    error: 'Възникна проблем при изтриването на записа, моля опитайте отново.'
                                }), content_type = "application/json")

            return HttpResponse(json.dumps('Success'), content_type = "application/json")

    raise Http404

def upload_csv(request):
    if(request.is_ajax()):
        if(request.method == 'POST'):
            stuff = list(request.POST.iterlists())
            objects = json.loads(stuff[0][0].encode('utf-8'))
            Mentor.create_from_upload(objects)

            return HttpResponse(json.dumps({
                                    'redir': '/mentors'
                                }))

    raise Http404

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

    return asbtr_preview_csv(request, view, choices)