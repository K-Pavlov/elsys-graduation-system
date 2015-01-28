from django.forms import ModelForm

from ..models.mentor import Mentor

class MentorForm(ModelForm):
    class Meta:
        model = Mentor
        fields = ['teacher', 'season', ]