from django.forms import ModelForm

from graduation_system_app.models.mentor import Mentor

class MentorForm(ModelForm):
    class Meta:
        model = Mentor