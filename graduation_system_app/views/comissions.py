# -*- coding: utf-8 -*-
import json
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import render_to_string


from common import create_from_form_post, create_from_form_edit, get_pair, asbtr_preview_csv, paginate, abstr_all
from ..forms import SeasonYearsOnly, ComissionForm, UploadForm
from ..common.pdf_renderer import render_to_pdf
from ..models.season import Season
from ..models.comission import Comission

def all(request):
    view_info = {
        'model': Comission,
        'title': u'Ръководители',
        'table_template': 'comissions/_table.html',
    }

    urls = {
        'create': 'create_comission',
        'edit': 'edit_comission',
        'delete': 'delete_comission',
        'preview': 'preview_comissions',
    }

    return abstr_all(request, urls, view_info)

def get_page(request, page_num):
    if(request.is_ajax()):
        page = paginate(page_num, Comission)
        html = render_to_string('comissions/_table.html', {
            'objects': page,
            'urls': {
                'edit': 'edit_comission',
                'delete': 'delete_comission',
            },
        })

        return HttpResponse(html)

def edit(request, id):
    comission = Comission.objects.filter(id=id)
    if not id or not comission.exists():
        return HttpResponseRedirect('/comissions/create')
    else: 
        context_data = {
            'title': u'Промени комисия',
            'year': datetime.now().year,
            'id': comission[0].id,
            'season_form': SeasonYearsOnly()
        }
        return create_from_form_edit(request, ComissionForm, 
                            'all_comissions', 
                            'comissions/edit.html', 
                            context_data,
                            comission[0])

def create(request):
    context_data = {
            'title': u'Създай комисия',
            'year': datetime.now().year,
            'season_form': SeasonYearsOnly()
        }

    return create_from_form_post(request, ComissionForm, 
                            'all_comissions', 
                            'comissions/create.html', 
                            context_data)

def delete(request, id):
    if request.is_ajax():
        try:
            comission = Comission.objects.get(id=id)
            comission.soft_delete()
        except Comission.DoesNotExist:
            return HttpResponseNotFound(json.dumps({
                                    error: 'Възникна проблем при изтриването на записа, моля опитайте отново.'
                                }), content_type = "application/json")

        return HttpResponse(json.dumps('Success'), content_type = "application/json")

    raise Http404

def upload_csv(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            Comission.from_csv(form.cleaned_data['file'])
    return HttpResponseRedirect(reverse('all_comissions'))

def preview_csv(request):
    view = {
        'title': 'Ръководители',
        'name': 'mentors',
        'model': Mentor,
    }

    choices = [get_pair('Фирма', 'firm'), get_pair('Име', 'fname'),
               get_pair('Презиме', 'mname'), get_pair('Фамилия', 'lname')]

    return asbtr_preview_csv(request, view, choices)

def generate_protocol(request):
    context = {
        'comissions': Comission.objects.all()
    }
    return render_to_pdf('comissions/comissions_table.html', context)
   