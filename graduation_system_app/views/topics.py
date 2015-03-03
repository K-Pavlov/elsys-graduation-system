# -*- coding: utf-8 -*-
import json
import csv
from datetime import datetime
 
from django.core.urlresolvers import reverse
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import render_to_string
 
from common import create_from_form_post, create_from_form_edit, get_pair, asbtr_preview_csv, paginate, abstr_all
from ..forms import SeasonYearsOnly, TopicForm, UploadForm
from ..models.season import Season
from ..models.topic import Topic
 
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
    topic = Topic.objects.filter(id=id)
    if not id or not topic.exists():
        return HttpResponseRedirect('/topics/create')
    else:
        context_data = {
            'title': u'Променете тема',
            'year': datetime.now().year,
            'id': topic[0].id,
            'season_form': SeasonYearsOnly()
        }
        return create_from_form_edit(request, TopicForm,
                            'all_topics',
                            'edit.html',
                            context_data,
                            topic[0])
 
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
    if request.is_ajax():
        try:
            topic = Topic.objects.get(id=id)
            topic.soft_delete()
        except Topic.DoesNotExist:
            return HttpResponseNotFound(json.dumps({
                                    error: 'Възникна проблем при изтриването на записа, моля опитайте отново.'
                                }), content_type = "application/json")
 
        return HttpResponse(json.dumps('Success'), content_type = "application/json")
 
    raise Http404
 
def upload_csv(request):
    if(request.is_ajax()):
        if(request.method == 'POST'):
            post_as_list = list(request.POST.iterlists())
            # Elements in the list are tuples 
            topic_tuple = post_as_list[0]

            # So we need need the first argument of the tuple
            # which holds our json data
            topic_data = topic_tuple[0]

            objects = json.loads(topic_data.encode('utf-8'))
            Topic.create_from_upload(objects)

            return HttpResponse(json.dumps({
                                    'redir': '/topics'
                                }))

    raise Http404

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

    return asbtr_preview_csv(request, view, choices)