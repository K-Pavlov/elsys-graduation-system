# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import smart_bytes

from .firm import Firm
from .season import Season
from ..common.uuid_generator import make_uuid_charfield

class Teacher(models.Model):
    id = make_uuid_charfield() 
    first_name = models.CharField(verbose_name='Име', max_length=50)
    middle_name = models.CharField(verbose_name='Презиме', max_length=50, blank=True, null=True, default='')
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    firm = models.ForeignKey(Firm, verbose_name='Фирма', blank=True,
                            null=True, default='', related_name='referees',
                            on_delete=models.SET_NULL,)

    def save(self, *args, **kwargs):
        current_season = Season.objects.get(is_active=True)
        self.season = Season.objects.get(is_active=True)
        super(Teacher, self).save(*args, **kwargs)

    def __str__(self):
        string = u"%s %s %s" % (self.first_name, self.middle_name, self.last_name)
        return smart_bytes(string)

    class Meta:
        app_label = "graduation_system_app"