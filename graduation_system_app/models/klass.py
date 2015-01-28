# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import smart_bytes

from ..common.uuid_generator import make_uuid_charfield

class Klass(models.Model):
    id = make_uuid_charfield() 
    letter = models.CharField(verbose_name='Паралелка', max_length=100)
    specialization = models.CharField(verbose_name= 'Специалност', max_length= 100)

    def __str__(self):
        string = u"%s %s" % (self.letter, self.specialization)
        return smart_bytes(string)

    class Meta:
        app_label = "graduation_system_app"