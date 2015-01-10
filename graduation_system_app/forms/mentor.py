from django.forms import ModelForm

from ..models.mentor import Mentor

class MentorForm(ModelForm):
    class Meta:
        model = Mentor
        fields = ['first_name','middle_name','last_name',]

    def __init__(self, *args, **kwargs):
        super(SampleClass, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'my_class'