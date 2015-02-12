# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import smart_bytes

from deletable_model import DeletableModelBase

class Firm(DeletableModelBase): 
    name = models.CharField(verbose_name='Име', max_length=100)

    def __str__(self):
        return smart_bytes(self.name)

    class Meta:
        app_label = "graduation_system_app"