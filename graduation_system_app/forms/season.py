# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from ..models.mentor import Season

class SeasonForm(ModelForm):
    class Meta:
        model = Season
        exclude = ('id')

class SeasonYearsOnly(forms.Form):
    years = forms.ChoiceField(choices=[(x,x) for x in Season.objects.all()], label='Сезон:')
    
    def __init__(self, *args, **kwargs):
        super(SeasonYearsOnly, self).__init__(*args, **kwargs)
        try:
            print([(x,x) for x in Season.objects.all()])
            self.fields['years'].choices = [(x,x) for x in Season.objects.all()]
            self.fields['years'].choices.append(('all', 'Всички'))
            self.initial['years'] = Season.objects.get(is_active=True).year
        except Season.DoesNotExist:
            self.initial['years'] = 'all'
