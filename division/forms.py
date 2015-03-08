from global_constants import STANDARD_EXCLUDE_FORMS

from django import forms
from django.forms import ModelForm

from division.models.class_letter import ClassLetter
from division.models.mentor import Mentor
from division.models.specialization import Specialization
from division.models.student import Student
from division.models.topic import Topic

class ClassLetterForm(ModelForm):
    class Meta:
        model = ClassLetter
        exclude = STANDARD_EXCLUDE_FORMS

class MentorForm(ModelForm):
    class Meta:
        model = Mentor
        exclude = ('id', 'is_deleted', 'teacher')


class SpecializationForm(ModelForm):
    class Meta:
        model = Specialization
        exclude = STANDARD_EXCLUDE_FORMS

class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = STANDARD_EXCLUDE_FORMS

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        exclude = STANDARD_EXCLUDE_FORMS