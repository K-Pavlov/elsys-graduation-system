# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.encoding import smart_bytes

from shared.models.deletable_model import DeletableModelBase

class ClassLetter(DeletableModelBase):
    letter = models.CharField(verbose_name='Паралелка', max_length=100,)

    def soft_delete(self):
        self.students.clear()

        return super(ClassLetter, self).soft_delete()

    def validate_unique(self, *args, **kwargs):
        super(ClassLetter, self).validate_unique(*args, **kwargs)
        print 'here'
        if(self.pk is not None):
            if(self.__class__.objects.filter(letter=self.letter).exists()):
                raise ValidationError(
                    {
                        'letter': ('Паралелка със буква вече съществува',)
                    }
                )

    def __str__(self):
        string = u'%s' % (self.letter)
        return smart_bytes(string)
    
    class Meta:
        app_label = 'division'
        db_table = 'class_letter'
        ordering = ['letter']