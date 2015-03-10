# -*- coding: utf-8 -*-
import csv

from django.db import models
from django.utils.encoding import smart_bytes

from shared.models.season_model import SeasonModelBase
from shared.models.season import Season
from shared.models.firm import Firm
from shared.models.teacher import Teacher

class Comission(SeasonModelBase):
    members_of_comission = models.ManyToManyField(Teacher, verbose_name='Членове на комисията', blank=True,
                            null=True, default='', related_name='members_of_comission',)
    start_time = models.DateTimeField(auto_now_add=False, blank=True, null=True, default='', verbose_name='Начален час')
    head_of_comission = models.OneToOneField(Teacher, verbose_name='Председател на комисията', blank=True,
                            null=True, default='', related_name='head_of_comission',
                            on_delete=models.SET_NULL,)

    def soft_delete(self):
        self.head_of_comission = None
        self.students.clear()
        self.members_of_comission.clear()

        return super(Comission, self).soft_delete()

    def __str__(self):
        return smart_bytes('Председател ' + self.head_of_comission.__str__())

    class Meta:
        app_label = 'defences'
        db_table = 'comission'
        ordering = ['start_time']