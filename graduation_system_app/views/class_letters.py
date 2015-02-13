# -*- coding: utf-8 -*-
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

from common import create_from_form_post, create_from_form_edit
from ..forms.season import SeasonYearsOnly
from ..forms.klass import ClassLetterForm
from ..forms.file import UploadForm
from ..models.season import Season
from ..models.class_letter import ClassLetter

def all(request):
    return render(
        request,
        'class_letters/all.html',
        context_instance = RequestContext(request,
        {
            'title': u'Паралелки',
            'year': datetime.now().year,
            'class_letters': ClassLetter.objects.all(),
            'season_form': SeasonYearsOnly(),
        })
    )

def edit(request, id):
    class_letter = ClassLetter.objects.filter(id=id)
    if not id or not class_letter.exists():
        return HttpResponseRedirect('/class_letters/create')
    else: 
        context_data = {
            'title': u'Промени паралелка',
            'year': datetime.now().year,
            'id': class_letter[0].id,
            'season_form': SeasonYearsOnly(),
        }

        return create_from_form_edit(request, ClassLetterForm, 
                            'all_class_letters', 
                            'edit.html',
                            context_data,
                            class_letter[0])

def create(request):
    context_data = {
            'title': u'Създай паралелка',
            'year': datetime.now().year,
            'season_form': SeasonYearsOnly(),
        }

    return create_from_form_post(request, ClassLetterForm, 
                            'all_class_letters', 
                            'create.html',
                            context_data)

def delete(request, id):
    if request.is_ajax():
        if request.method == 'DELETE':
            try:
                class_letter = ClassLetter.objects.get(id=id)
                class_letter.soft_delete()
            except ClassLetter.DoesNotExist:
                return HttpResponseNotFound(json.dumps({
                                    error: 'Възникна проблем при изтриването на записа, моля опитайте отново.'
                                }), content_type = "application/json")

            return HttpResponse(json.dumps('Success'), content_type = "application/json")

    return HttpResponseNotFound(json.dumps({
                                    error: 'Възникна проблем при изтриването на записа, моля опитайте отново.'
                                }), content_type = "application/json")



