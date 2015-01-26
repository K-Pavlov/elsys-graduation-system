from django.forms import ModelForm

from ..models.referee import Referee

class RefereeForm(ModelForm):
    class Meta:
        model = Referee
        fields = ['first_name','middle_name','last_name', 'firm', 'season', ]