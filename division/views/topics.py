# -*- coding: utf-8 -*-
import json
import csv
from datetime import datetime
 
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.template.loader import render_to_string

from division.forms import TopicForm
from division.models.topic import Topic
from shared.forms import SeasonYearsOnly, UploadForm
from shared.models.season import Season
from common.views import create_from_form_post, create_from_form_edit, get_pair, paginate
from common.views import abstr_all, abstr_delete, abstr_preview_csv, abstr_upload_data
 
def all(request):
    view_info = {
        'model': Topic,
        'title': u'Теми',
        'table_template': 'topics/_table.html',
    }

    urls = {
        'create': 'create_topic',
        'edit': 'edit_topic',
        'delete': 'delete_topic',
        'preview': 'preview_topics',
    }

    return abstr_all(request, urls, view_info)

def get_page(request, page_num):
    if(request.is_ajax()):
        page = paginate(page_num, Topic)
        html = render_to_string('topics/_table.html',RequestContext(request, {
            'objects': page,
            'urls': {
                'edit': 'edit_topic',
                'delete': 'delete_topic',
            },
        }))

        return HttpResponse(html)
 
def edit(request, id):
    topic = get_object_or_404(Topic, pk=id)
    context_data = {
        'title': u'Променете тема',
        'year': datetime.now().year,
        'id': topic.id,
        'season_form': SeasonYearsOnly()
    }

    return create_from_form_edit(request, TopicForm,
                        'all_topics',
                        'edit.html',
                        context_data,
                        topic)
 
def create(request):
    context_data = {
            'title': u'Създайте тема',
            'year': datetime.now().year,
            'season_form': SeasonYearsOnly(),
        }
 
    return create_from_form_post(request, TopicForm,
                            'all_topics',
                            'create.html',
                            context_data)
 
def delete(request, id):
    return abstr_delete(request, id, Topic)
 
def upload_csv(request):
    return abstr_upload_data(request, Topic, '/topics')

def preview_csv(request):
    view = {
        'title': 'Теми',
        'name': 'topics',
        'model': Topic,
    }

    choices = [get_pair('-' * 9, ''),
               get_pair('Заглавие', 'title'), 
               get_pair('Описание', 'description'),
               get_pair('Име на ръководител', 'fname'),
               get_pair('Презиме на ръководител', 'mname'),
               get_pair('Фамилия на ръководител', 'lname'),
               get_pair('Фирма на ръководител', 'firm'),]

    return abstr_preview_csv(request, view, choices)