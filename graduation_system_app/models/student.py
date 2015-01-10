# -*- coding: utf-8 -*-

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .mentor import Mentor
from .topic import Topic
from ..common.uuid_generator import make_uuid_charfield

class Student(models.Model):
    id = make_uuid_charfield()
    first_name = models.CharField(verbose_name='Име', max_length=50)
    middle_name = models.CharField(verbose_name='Презиме', max_length=50, blank=True, null=True, default='')
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    class_letter = models.CharField(verbose_name='Клас', max_length=1, blank=True, null=True, default='')
    specialization = models.CharField(verbose_name='Специалност', max_length=150, blank=True, null=True, default='')
    topic = models.ForeignKey(Topic, verbose_name='Тема', blank=True, null=True, related_name='students')
    mentor = models.ForeignKey(Mentor, verbose_name='Дипломен ръководител', blank=True, null=True, related_name='students')
    grade = models.FloatField(verbose_name='Оценка',
        validators=[MinValueValidator(2.0), MaxValueValidator(6.0)], blank=True, default=2.0)

    def __str__(self):
            return u"%s %s %s" % (self.first_name, self.middle_name, self.last_name)

    @staticmethod
    def from_csv(csvfile):
        pass

    class Meta:
        app_label = "graduation_system_app"


