from django.forms import ModelForm

from ..models.firm import Firm

class FirmForm(ModelForm):
    class Meta:
        model = Firm
        exclude = ('id')