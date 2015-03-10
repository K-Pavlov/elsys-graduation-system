# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import smart_bytes

from shared.models.deletable_model import DeletableModelBase

class Specialization(DeletableModelBase):
    name = models.CharField(verbose_name= 'Име', max_length= 100)

    def soft_delete(self):
        self.students.clear()
        return super(Specialization, self).soft_delete()

    def __str__(self):
        string = u'%s' % (self.name)
        return smart_bytes(string)

    class Meta:
        app_label = 'division'
        db_table = 'specialization'
        ordering = ['name']
