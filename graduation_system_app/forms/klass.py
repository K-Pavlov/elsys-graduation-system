from django.forms import ModelForm

from ..models.klass import Klass

class KlassForm(ModelForm):
    class Meta:
        model = Klass
        fields = ['letter', 'specialization']