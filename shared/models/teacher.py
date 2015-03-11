# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
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
                            null=True, default='', related_name='teachers',
                            on_delete=models.SET_NULL,)

    def soft_delete(self):
        self.firm = None
        self.members_of_comission.clear()
        for referee in self.referees.all():
            referee.soft_delete()

        for mentor in self.mentors.all():
            mentor.soft_delete()

        return super(Teacher, self).soft_delete()

    def __str__(self):
        string = u'%s %s %s' % (self.first_name, self.middle_name, self.last_name)
        return smart_bytes(string)

    class Meta:
        app_label = 'shared'
        db_table = 'teacher'
        ordering = ['first_name', 'middle_name', 'last_name']