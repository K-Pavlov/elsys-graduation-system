# -*- coding: utf-8 -*-
import csv
from pprint import pprint

from django.db import models
from django.utils.encoding import smart_bytes

from common import create_mentor_referee
from .season import Season
from .firm import Firm
from .teacher import Teacher
from ..common.uuid_generator import make_uuid_charfield

class Mentor(models.Model):
    id = make_uuid_charfield() 
    teacher = models.ForeignKey(Teacher, verbose_name='Учител', blank=True,
                            null=True, default='', related_name='mentors',)
    season = models.ForeignKey(Season, verbose_name='Сезон', blank=True,
                            null=True, default='', related_name='mentors',
                            on_delete=models.SET_NULL,)

    def save(self, *args, **kwargs):
        try:
            self.season = Season.objects.get(is_active=True)
        except Season.DoesNotExist:
            pass
        super(Mentor, self).save(*args, **kwargs)

    @staticmethod
    def create_from_upload(objects):
        i = 0
        created_model = []
        for mentor_dict in objects:
            model = Mentor.create(mentor_dict)
            if(model and not Mentor.objects.filter(id=model.id).exists()):
                created_model.append(model)
                i += 1

            if (i % 50 == 0):
                Mentor.objects.bulk_create(created_model)
                created_model = []
 
        if (created_model.count != 0):
            Mentor.objects.bulk_create(created_model)
    
    @staticmethod
    def create(mentor_dict):
        return create_mentor_referee(Mentor, mentor_dict)

    def __str__(self):
        return self.teacher.__str__()

    class Meta:
        app_label = "graduation_system_app"