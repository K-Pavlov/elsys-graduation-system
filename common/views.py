# -*- coding: utf-8 -*-
import json
import csv
from datetime import datetime

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.forms.util import ErrorList
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render
from django.template import RequestContext

from shared.forms import UploadForm, SeasonYearsOnly
from shared.models.teacher import Teacher

def abstr_all(request, urls, view_info):
    page = paginate(1, view_info['model'])

    return render(request,
        'all.html',
        context_instance = RequestContext(request,
        {
            'title': view_info['title'],
            'year': datetime.now().year,
            'objects': page,
            'table_template': view_info['table_template'],
            'urls': urls,
            'upload_form': UploadForm(),
            'season_form': SeasonYearsOnly(),
        }))

def paginate(page, model):
    model_list = model.objects.all()
    paginator = Paginator(model_list, 20) # Show 20 items per page
    
    try: 
        page = int(page)
    except ValueError:
        page = 1

    try:
        models = paginator.page(page)
    except EmptyPage:
        models = paginator.page(paginator.num_pages)

    range_gap = 2
    if(page > range_gap):
        start = page - range_gap
    else:
        start = 1

    if(start == 1):
        end = 5 if 5 < paginator.num_pages else paginator.num_pages
    elif(page < paginator.num_pages - range_gap):
        end = page + range_gap
    else:
        end = paginator.num_pages
        start = end - 4

    models.pages = range(start, end + 1)

    return models

def create_from_form_post(request, model_form, redir_view_name, template, context_data):
    if(request.method == 'POST'):
        form = model_form(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect(reverse(redir_view_name))
    else:
        form = model_form()

    return handle_invalid_model(form, context_data, request, template)

def create_from_form_edit(request, model_form, redir_view_name, template, context_data, instance):
    if(request.method == 'POST'):
        form = model_form(request.POST, instance=instance)

        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect(reverse(redir_view_name))
    else:
        form = model_form(instance=instance)

    return handle_invalid_model(form, context_data, request, template)

def handle_invalid_model(form, context_data, request, template) :
    context_data['form'] = form
    return render(request,
        template,
        context_instance = RequestContext(request, context_data))

def handle_form_mentor_ref(instance_form, teacher_form, model):
    teacher = teacher_form.save(commit=False)
    if(teacher_form.is_valid() and instance_form.is_valid()):
        try:
            teacher = Teacher.objects.get(first_name=teacher.first_name,
                                            middle_name=teacher.middle_name,
                                            last_name=teacher.last_name)
        except Teacher.DoesNotExist:
            teacher.save()

        instance = save_form_mentor_ref(instance_form, teacher, model)
        if(not instance):
            errors = instance_form._errors.setdefault('__all__', ErrorList())
            errors.append(u'Запис със същитите имена вече съществува')
            return False
        else:
            return True

def handle_edit_mentor_ref(instance_form, teacher_form, model):
    teacher = teacher_form.save(commit=False)
    if(teacher_form.is_valid() and instance_form.is_valid()):
        try:
            teacher = Teacher.objects.get(first_name=teacher.first_name,
                                            middle_name=teacher.middle_name,
                                            last_name=teacher.last_name)
        except Teacher.DoesNotExist:
            teacher.save()

        instance_data = instance_form.save()
        instance = model.objects.get(teacher=teacher, season=instance_data.season)
        if(not instance.id == instance_data.id):
                errors = instance_form._errors.setdefault('__all__', ErrorList())
                errors.append(u'Запис със същитите имена вече съществува')
                return False
        else:
                return True

def save_form_mentor_ref(form, teacher, model):
    try:
        instance_data = form.save(commit=False)
        instance = model.objects.get(teacher=teacher, season=instance_data.season)

        return False
    except model.DoesNotExist:
        instance = model()
        instance.teacher = teacher
        instance.season = instance_data.season
        instance.save()

        return instance

def abstr_delete(request, id, model):
    if(request.is_ajax()):
        try:
            instance = model.objects.get(id=id)
            instance.soft_delete()
        except model.DoesNotExist:
            return HttpResponseNotFound(json.dumps({
                                    error: 'Възникна проблем при изтриването на записа, моля опитайте отново.'
                                }), content_type = "application/json")

        return HttpResponse(json.dumps('Success'), content_type = "application/json")

    raise Http404

def abstr_preview_csv(request, view, choices):
    form = UploadForm()
    if(request.method == 'POST'):
        form = UploadForm(request.POST, request.FILES)
        if(form.is_valid()):
            reader = csv.reader(form.cleaned_data['file'])
            headers = reader.next()

            return render(request,
                'preview-csv.html',
                context_instance = RequestContext(request,
                {
                    'title': 'Преглед на ' + view['title'],
                    'year': datetime.now().year,
                    'choices': choices,
                    'headers': headers,
                    'view_name': view['name'],
                    'rows': reader,
                    'season_form': SeasonYearsOnly()
                }))

    return render(request,
        view['name'] + '/all.html',
        context_instance = RequestContext(request,
        {
            'title': view['title'],
            'year': datetime.now().year,
            view['name']: view['model'].objects.all(),
            'upload_form': form,
            'season_form': SeasonYearsOnly(),
        }))

def abstr_upload_data(request, model, redir):
    if(request.is_ajax()):
        if(request.method == 'POST'):
            post_as_list = list(request.POST.iterlists())
            # Elements in the list are tuples 
            model_tuple = post_as_list[0]

            # So we need need the first argument of the tuple
            # which holds our json data
            model_data = model_tuple[0]

            objects = json.loads(model_data.encode('utf-8'))
            model.create_from_upload(objects)

            return HttpResponse(json.dumps({
                                    'redir': redir
                                }))

    raise Http404

def get_pair(name, value):
    return {
        'name': name,
        'value': value,
    }

def handler404(request):
    return HttpResponseNotFound('404.html', context_instance=RequestContext(request))


def handler500(request):
    return HttpResponseServerError('500.html', context_instance=RequestContext(request))