# -*- coding: utf-8 -*-
import time
import datetime

from django.db import models
from django.utils.encoding import smart_bytes
from django.utils.translation import gettext as _
from south.modelsinspector import add_introspection_rules

from ..common.uuid_generator import make_uuid_charfield

add_introspection_rules([], ["^graduation_system_app\.models\.season\.YearYearField"])
class YearYearField(models.CharField):
    default_error_messages = {
        'invalid': _('Format year/year.'),
    }

    def __init__(self, input_formats=None, *args, **kwargs):
        super(YearYearField, self).__init__(*args, **kwargs)
        self.input_formats = input_formats

    def clean(self, value):
        input_format = '%Y/%Y'
        if value in validators.EMPTY_VALUES:
            return None
        try:
            date = datetime.date(*time.strptime(value, input_format)[:3])
            return format(date, input_format)
        except ValueError:
            raise ValidationError(self.error_messages['invalid'])

class Season(models.Model):
    id = make_uuid_charfield() 
    year = YearYearField(verbose_name='?????', max_length= 20)

    def __str__(self):
        string = u"%s" % (self.year)
        return smart_bytes(string)

    class Meta:
        app_label = "graduation_system_app"
