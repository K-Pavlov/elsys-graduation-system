# -*- coding: utf-8 -*-

from django.forms import ModelForm

from ..models.teacher import Teacher

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        exclude = ('id')