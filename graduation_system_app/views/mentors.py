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

from common import create_from_form_post, create_from_form_edit, get_pair, asbtr_preview_csv
from ..forms.season import SeasonYearsOnly
from ..forms.mentor import MentorForm
from ..forms.file import UploadForm
from ..models.season import Season
from ..models.mentor import Mentor

def all(request):
    return render(request,
        'mentors/all.html',
        context_instance = RequestContext(request,
        {
            'title': u'Ръководители',
            'year': datetime.now().year,
            'mentors': Mentor.objects.all(),
            'upload_form': UploadForm(),
            'season_form': SeasonYearsOnly(),
        }))

def edit(request, id):
    mentor = Mentor.objects.filter(id=id)
    if not id or not mentor.exists():
        return HttpResponseRedirect('/mentors/create')
    else: 
        context_data = {
            'title': u'Промени ръководител',
            'year': datetime.now().year,
            'id': mentor[0].id,
            'season_form': SeasonYearsOnly(),
        }

        return create_from_form_edit(request, MentorForm, 
                            'all_mentors', 
                            'edit.html',
                            context_data,
                            mentor[0])

def create(request):
    context_data = {
            'title': u'Създай ръководител',
            'year': datetime.now().year,
            'season_form': SeasonYearsOnly(),
        }

    return create_from_form_post(request, MentorForm, 
                            'all_mentors', 
                            'create.html',
                            context_data)

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

    return HttpResponseNotFound(json.dumps({
                                    error: 'Възникна проблем при изтриването на записа, моля опитайте отново.'
                                }), content_type = "application/json")

def upload_csv(request):
    if(request.is_ajax()):
        if(request.method == 'POST'):
            stuff = list(request.POST.iterlists())
            objects = json.loads(stuff[0][0].encode('utf-8'))
            Mentor.create_from_upload(objects)

    return HttpResponseRedirect(reverse('all_mentors'))

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