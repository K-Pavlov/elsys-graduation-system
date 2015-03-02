# -*- coding: utf-8 -*-
import csv

from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import smart_bytes

from mentor_referee_creator import create_mentor_referee
from season_model import SeasonModelBase
from deletable_model import DeletableModelBase, DeletableManager
from season import Season
from firm import Firm
from teacher import Teacher

class Referee(SeasonModelBase):
    teacher = models.ForeignKey(Teacher, verbose_name='Учител', blank=True,
                            null=True, default='', related_name='referees',)
    email = models.EmailField(verbose_name='Имейл', max_length=254)

    def soft_delete(self):
        self.topics.clear()
        self.students.clear()

        return super(Referee, self).clean()

    @staticmethod
    def create_from_upload(objects):
        i = 0
        created_model = []
        for referee_dict in objects:
            model = Referee.create(referee_dict)
            if(model and not Referee.objects.filter(id=model.id).exists()):
                try:
                    model.email = referee_dict['email']
                except:
                    pass

                created_model.append(model)
                i += 1

            if (i % 50 == 0):
                Referee.objects.bulk_create(created_model)
                created_model = []
 
        if (created_model.count != 0):
            Referee.objects.bulk_create(created_model)

    @staticmethod
    def create(referee_dict):
        return create_mentor_referee(Referee, referee_dict)

    def __str__(self):
        return self.teacher.__str__()

    class Meta:
        app_label = "graduation_system_app"
        db_table = "referee"

def get_upload_path(instance, filename):
    return u"referee_%s/%s" % (instance.referee.id, filename)

class Referal(DeletableModelBase):
    file = models.FileField(verbose_name='Рецензия', upload_to=get_upload_path, blank=True, null=True)
    referee = models.ForeignKey(Referee, verbose_name='Учител', blank=True,
                            null=True, default='', related_name='referals',
                            on_delete=models.SET_NULL,)

    class Meta:
        app_label = "graduation_system_app"
        db_table = "referal"