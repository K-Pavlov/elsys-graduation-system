# -*- coding: utf-8 -*-
import csv

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.encoding import smart_bytes

from shared.models.model_creator import create_mentor_referee
from shared.models.season_model import SeasonModelBase
from shared.models.season import Season
from shared.models.firm import Firm
from shared.models.teacher import Teacher

class Mentor(SeasonModelBase):
    teacher = models.ForeignKey(Teacher, verbose_name='Учител', blank=True,
                            null=True, default='', related_name='mentors',)

    def soft_delete(self):
        self.students.clear()
        self.topics.clear()

        return super(Mentor, self).soft_delete()

    @staticmethod
    def create_from_upload(objects):
        i = 0
        created_model = []
        for mentor_dict in objects:
            model = Mentor.create(mentor_dict)
            if(model and not Mentor.objects.filter(id=model.id).exists()):
                created_model.append(model)
                i += 1

            if(i % 50 == 0):
                Mentor.objects.bulk_create(created_model)
                created_model = []
 
        if(created_model.count != 0):
            Mentor.objects.bulk_create(created_model)
    
    @staticmethod
    def create(mentor_dict):
        return create_mentor_referee(Mentor, mentor_dict)

    def __str__(self):
        return self.teacher.__str__()

    class Meta:
        app_label = 'division'
        db_table = 'mentor'
        ordering = ['teacher']