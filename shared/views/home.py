# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from shared.forms import SeasonYearsOnly
from shared.models.season import Season

def index(request):
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
