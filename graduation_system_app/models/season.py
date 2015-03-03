# -*- coding: utf-8 -*-
import time
import datetime

from django.db import models
from django.utils.encoding import smart_bytes
from django.utils.translation import gettext as _

from deletable_model import DeletableModelBase

class Season(DeletableModelBase):
    year = models.CharField(verbose_name='Година', max_length= 20)
    is_active = models.NullBooleanField(verbose_name='Активен', default=False)

    def soft_delete(self):
        self.student_set.clear()
        self.referee_set.clear()
        self.topic_set.clear()
        self.mentor_set.clear()
        self.comission_set.clear()

        return super(Season, self).soft_delete()

    def save(self, *args, **kwargs):
        if self.is_active:
            try:
                temp = Season.objects.get(is_active=True)
                if self != temp:
                    temp.is_active = False
                    temp.save()
            except Season.DoesNotExist:
                pass
        super(Season, self).save(*args, **kwargs)

    def __str__(self):
        string = u"%s" % (self.year)
        return smart_bytes(string)

    class Meta:
        app_label = "graduation_system_app"
        db_table = "season"