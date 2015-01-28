# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from ..models.season import Season
from ..forms.season import SeasonYearsOnly

def index(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    current_season = Season.objects.get(is_active=True)
    return render(
        request,
        'index.html',
        context_instance = RequestContext(request,
        {
            'title': u'Система за дипломиране',
            'season': current_season.year,
            'year': datetime.now().year,
            'season_form': SeasonYearsOnly()
        })
    )