from django.forms import ModelForm

from ..models.referee import Referee

class RefereeForm(ModelForm):
    class Meta:
        model = Referee
        fields = ['teacher', 'referal', 'season', ]