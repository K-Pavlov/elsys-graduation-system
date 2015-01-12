from django.forms import ModelForm

from ..models.mentor import Season

class SeasonForm(ModelForm):
    class Meta:
        model = Season
        fields = ['year', 'is_active']