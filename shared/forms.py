# -*- coding: utf-8 -*-
from global_constants import STANDARD_EXCLUDE_FORMS

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from shared.models.firm import Firm
from shared.models.teacher import Teacher
from shared.models.season import Season

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class FirmForm(ModelForm):
    class Meta:
        model = Firm
        exclude = STANDARD_EXCLUDE_FORMS

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        exclude = STANDARD_EXCLUDE_FORMS

class SeasonYearsOnly(forms.Form):
    years = forms.ChoiceField(choices=[(x,x) for x in Season.objects.all()], label='Сезон:')
    
    def __init__(self, *args, **kwargs):
        super(SeasonYearsOnly, self).__init__(*args, **kwargs)
        try:
            self.fields['years'].choices = [(x,x) for x in Season.objects.all()]
            self.fields['years'].choices.append(('all', 'Всички'))
            self.initial['years'] = Season.objects.get(is_active=True).year
        except Season.DoesNotExist:
            self.initial['years'] = 'all'

class SeasonForm(ModelForm):
    class Meta:
        model = Season
        exclude = STANDARD_EXCLUDE_FORMS

class UploadForm(forms.Form):
    file  = forms.FileField()