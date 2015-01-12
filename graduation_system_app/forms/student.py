# -*- coding: utf-8 -*-

from django.forms import ModelForm

from ..models.student import Student

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name','middle_name','last_name', 
                  'class_letter', 'specialization', 'topic',
                  'mentor', 'grade']

