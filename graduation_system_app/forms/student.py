# -*- coding: utf-8 -*-

from django.forms import ModelForm

from ..models.student import Student

class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ('id')

