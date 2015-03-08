from global_constants import STANDARD_EXCLUDE_FORMS

from datetimewidget.widgets import DateTimeWidget
from django import forms
from django.forms import ModelForm

from defences.models import Comission
from division.models import Student

class ComissionForm(ModelForm):
    students = forms.ModelMultipleChoiceField(Student.objects.all(), required=False)
    class Meta:
        model = Comission
        exclude = STANDARD_EXCLUDE_FORMS
        widgets = {
            'start_time': DateTimeWidget(attrs={
                'id': 'date-picker'
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