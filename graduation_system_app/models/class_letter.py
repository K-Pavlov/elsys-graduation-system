# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import smart_bytes

from ..common.uuid_generator import make_uuid_charfield

class ClassLetter(models.Model):
    id = make_uuid_charfield() 
    letter = models.CharField(verbose_name='?????????', max_length=100)

    def __str__(self):
        string = u"%s" % (self.letter)
        return smart_bytes(string)

    class Meta:
        app_label = "graduation_system_app"