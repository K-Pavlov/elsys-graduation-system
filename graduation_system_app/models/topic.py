# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import smart_bytes
from ..common.uuid_generator import make_uuid_charfield

class Topic(models.Model):
    id = make_uuid_charfield()
    title = models.CharField(verbose_name='Заглавие', max_length=100)
    description = models.TextField(verbose_name='Описание', )

    @staticmethod
    def from_csv(csvfile):
        pass

    def __str__(self):
        string = u"%s" % self.title
        return smart_bytes(string)

    class Meta:
        app_label = "graduation_system_app"


