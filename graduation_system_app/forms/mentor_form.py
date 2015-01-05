from django.forms import ModelForm

from graduation_system_app.models.mentor import Mentor

class MentorForm(ModelForm):
    class Meta:
        model = Mentor
        fields = ['first_name','middle_name','last_name',]