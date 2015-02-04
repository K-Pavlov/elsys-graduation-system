# -*- coding: utf-8 -*-

from django.forms import ModelForm
from datetimewidget.widgets import DateTimeWidget

from ..models.comission import Comission

class ComissionForm(ModelForm):
    class Meta:
        model = Comission
        exclude = ('id')
        widgets = {
            'start_time': DateTimeWidget(attrs={'id':"date-picker"}, usel10n = True, bootstrap_version=3)
        }