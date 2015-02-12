from django.forms import ModelForm

from ..models.referee import Referal

class ReferalForm(ModelForm):
    class Meta:
        model = Referal
        exclude = ('id')