from django.forms import ModelForm

from ..models.specialization import Specialization
from ..models.class_letter import ClassLetter

class ClassLetterForm(ModelForm):
    class Meta:
        model = ClassLetter
        fields = ['letter']

class SpecializationForm(ModelForm):
    class Meta:
        model = Specialization
        fields = ['name']