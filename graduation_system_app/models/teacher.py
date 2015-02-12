# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import smart_bytes

from deletable_model import DeletableModelBase
from firm import Firm
from season import Season

class Teacher(DeletableModelBase):
    first_name = models.CharField(verbose_name='Име', max_length=50)
    middle_name = models.CharField(verbose_name='Презиме', max_length=50, blank=True, null=True, default='')
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    firm = models.ForeignKey(Firm, verbose_name='Фирма', blank=True,
                            null=True, default='', related_name='referees',
                            on_delete=models.SET_NULL,)

    def __str__(self):
        string = u"%s %s %s" % (self.first_name, self.middle_name, self.last_name)
        return smart_bytes(string)

    class Meta:
        app_label = "graduation_system_app"