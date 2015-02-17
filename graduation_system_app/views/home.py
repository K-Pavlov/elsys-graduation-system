# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from ..models.season import Season
from ..forms import SeasonYearsOnly
from django.contrib.admin.models import LogEntry

def index(request):
    logs = LogEntry.objects.all() #or you can filter, etc.
    for l in logs:
        print l
    return render(
        request,
        'index.html',
        context_instance = RequestContext(request,
        {
            'title': u'Система за дипломиране',
            'year': datetime.now().year,
            'season_form': SeasonYearsOnly()
        })
    )
