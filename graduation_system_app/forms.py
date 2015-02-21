# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from datetimewidget.widgets import DateTimeWidget

from models.teacher import Teacher
from models.student import Student
from models.referee import Referee
from models.mentor import Mentor
from models.specialization import Specialization
from models.class_letter import ClassLetter
from models.comission import Comission
from models.firm import Firm
from models.referee import Referal
from models.mentor import Season
from models.topic import Topic
from pprint import pprint

STANDARD_EXCLUDE = ('id', 'is_deleted')

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        exclude = STANDARD_EXCLUDE


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        exclude = STANDARD_EXCLUDE

class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = STANDARD_EXCLUDE

class SeasonForm(ModelForm):
    class Meta:
        model = Season
        exclude = STANDARD_EXCLUDE

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

class RefereeForm(ModelForm):
    class Meta:
        model = Referee
        exclude = STANDARD_EXCLUDE

class ReferalForm(ModelForm):
    class Meta:
        model = Referal
        exclude = STANDARD_EXCLUDE

class MentorForm(ModelForm):
    class Meta:
        model = Mentor
        exclude = STANDARD_EXCLUDE

class ClassLetterForm(ModelForm):
    class Meta:
        model = ClassLetter
        exclude = STANDARD_EXCLUDE

class SpecializationForm(ModelForm):
    class Meta:
        model = Specialization
        exclude = STANDARD_EXCLUDE

class FirmForm(ModelForm):
    class Meta:
        model = Firm
        exclude = STANDARD_EXCLUDE

class ComissionForm(ModelForm):
    students = forms.ModelMultipleChoiceField(Student.objects.all(), required=False)
    class Meta:
        model = Comission
        exclude = STANDARD_EXCLUDE
        widgets = {
            'start_time': DateTimeWidget(attrs={
                'id':"date-picker"
             }, usel10n = True, bootstrap_version=3,)
        }

    def __init__(self, *args, **kwargs):
        super(ComissionForm, self).__init__(*args, **kwargs)
        self.fields['students'].initial = self.instance.students.all()
        members_field = self.fields['members_of_comission']
        members_field.widget.attrs['size'] = members_field.queryset.count()
        pass

    def save(self, commit=True):
        instance = super(ComissionForm, self).save(commit=commit)
        instance.students = self.cleaned_data['students'] 
        if commit:
            instance.save()
        return instance

class UploadForm(forms.Form):
    file  = forms.FileField()

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