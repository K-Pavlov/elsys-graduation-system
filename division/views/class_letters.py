# -*- coding: utf-8 -*-
import json
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import render_to_string

from division.forms import ClassLetterForm
from division.models.class_letter import ClassLetter
from shared.forms import SeasonYearsOnly, UploadForm
from shared.models.season import Season
from common.views import create_from_form_post, create_from_form_edit, paginate, abstr_all

def all(request):
    view_info = {
        'model': ClassLetter,
        'title': u'Паралелки',
        'table_template': 'class_letters/_table.html',
    }

    urls = {
        'create': 'create_class_letter',
        'edit': 'edit_class_letter',
        'delete': 'delete_class_letter',
    }

    return abstr_all(request, urls, view_info)

def get_page(request, page_num):
    if(request.is_ajax()):
        page = paginate(page_num, ClassLetter)
        html = render_to_string('class_letters/_table.html', {
            'objects': page,
            'urls': {
                'edit': 'edit_class_letter',
                'delete': 'delete_class_letter',
            },
        })

        return HttpResponse(html)

def edit(request, id):
    class_letter = ClassLetter.objects.filter(id=id)
    if not id or not class_letter.exists():
        return HttpResponseRedirect('/class_letters/create')
    else: 
        context_data = {
            'title': u'Променете паралелка',
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
            'title': u'Създайте паралелка',
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

    raise Http404