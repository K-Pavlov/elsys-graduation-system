from global_constants import STANDARD_EXCLUDE_FORMS

from django.forms import ModelForm

from reviewing.models import Referee, Referal

class RefereeForm(ModelForm):
    class Meta:
        model = Referee
        exclude = ('id', 'is_deleted', 'teacher')

class ReferalForm(ModelForm):
    class Meta:
        model = Referal
        exclude = STANDARD_EXCLUDE_FORMS