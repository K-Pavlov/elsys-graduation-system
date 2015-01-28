# -*- coding: utf-8 -*-

from django.forms import ModelForm

from ..models.teacher import Teacher

class TeahcerForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name','middle_name','last_name', 'firm']