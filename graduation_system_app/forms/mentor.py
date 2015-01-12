from django.forms import ModelForm

from ..models.mentor import Mentor

class MentorForm(ModelForm):
    class Meta:
        model = Mentor
        fields = ['first_name','middle_name','last_name', 'season', ]