# -*- coding: utf-8 -*-
import time
import datetime

from django.db import models
from django.utils.encoding import smart_bytes
from django.utils.translation import gettext as _
from south.modelsinspector import add_introspection_rules

from ..common.uuid_generator import make_uuid_charfield

class Season(models.Model):
    id = make_uuid_charfield() 
    year = models.CharField(verbose_name='Година', max_length= 20)
    is_active = models.NullBooleanField(verbose_name='Активен', default=False)

    def __str__(self):
        string = u"%s" % (self.year)
        return smart_bytes(string)

    class Meta:
        app_label = "graduation_system_app"
