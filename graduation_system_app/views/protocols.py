# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import json
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import render_to_string

from common import create_from_form_post, create_from_form_edit, get_pair, asbtr_preview_csv, paginate, abstr_all
from ..common.pdf_renderer import render_to_pdf
from ..forms import StudentForm, UploadForm, SeasonYearsOnly
from ..models.season import Season
from ..models.student import Student
from ..models.comission import Comission


def all_students(request):
    year = ''
    try:
        year = Season.objects.get(is_active=True).year.split('/')[1]
    except Season.DoesNotExist:
        pass

    context = {
        'students': Student.objects.all(),
        'year': year,
    }
    return render_to_pdf('protocols/all_students.html', context)

def comission_with_students(request, id):
    try:
        comission = Comission.objects.get(id=id)
    except Comission.DoesNotExist:
        raise Http404

    print comission.start_time

    start_time = comission.start_time

    date = ''
    time = ''
    if(start_time):
        date = str(start_time.day) + '.' + str(start_time.month) + '.' + str(start_time.year)
        time = str(start_time.hour) + ':' + str(start_time.minute)

    context = {
        'comission': comission,
        'date': date,
        'time': time,
    }

    return render_to_pdf('protocols/comission_with_students.html', context)