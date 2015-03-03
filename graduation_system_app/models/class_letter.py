# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import smart_bytes

from deletable_model import DeletableModelBase

class ClassLetter(DeletableModelBase):
    letter = models.CharField(verbose_name='Паралелка', max_length=100)

    def soft_delete(self):
        self.students.clear()

        return super(ClassLetter, self).soft_delete()

    def __str__(self):
        string = u"%s" % (self.letter)
        return smart_bytes(string)
    
    class Meta:
        app_label = "graduation_system_app"
        db_table = "class_letter"