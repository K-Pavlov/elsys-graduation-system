# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.encoding import smart_bytes

from shared.models.deletable_model import DeletableModelBase

class Protocol(DeletableModelBase):
    name = models.CharField(verbose_name='Име', max_length=100)
    path_to_view = models.CharField(verbose_name='Път до изглед', max_length=100)

    def soft_delete(self):
        self.specializations.clear()
        return super(Protocol, self).soft_delete()

    def __str__(self):
       return smart_bytes(self.name)

    class Meta:
        app_label = 'division'
        db_table = 'protocol'
        ordering = ['name']

class Specialization(DeletableModelBase):
    name = models.CharField(verbose_name='Име', max_length=100)
    protocol = models.ForeignKey(Protocol, verbose_name='Вид протокол', blank=True,
                                 null=True, default='', related_name='specializations',)

    def soft_delete(self):
        self.students.clear()
        return super(Specialization, self).soft_delete()

    def validate_unique(self, *args, **kwargs):
        super(Specialization, self).validate_unique(*args, **kwargs)
        if(self.pk is not None):
            if(self.__class__.objects.filter(name=self.name).exists()):
                raise ValidationError(
                    {
                        'name': ('Специалност със същото име вече съществува',)
                    }
                )

    def __str__(self):
        return smart_bytes(self.name)

    class Meta:
        app_label = 'division'
        db_table = 'specialization'
        ordering = ['name']