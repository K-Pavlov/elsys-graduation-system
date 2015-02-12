# -*- coding: utf-8 -*-
import csv

from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import smart_bytes

from common import create_mentor_referee
from .season import Season
from .firm import Firm
from .teacher import Teacher
from ..common.uuid_generator import make_uuid_charfield

class Referee(models.Model):
    id = make_uuid_charfield() 
    teacher = models.ForeignKey(Teacher, verbose_name='Учител', blank=True,
                            null=True, default='', related_name='referees',)
    email = models.EmailField(verbose_name='Имейл', max_length=254)
    season = models.ForeignKey(Season, verbose_name='Сезон', blank=True,
                            null=True, default='', related_name='referees',
                            on_delete=models.SET_NULL,)

    def save(self, *args, **kwargs):
        try:
            self.season = Season.objects.get(is_active=True)
        except Season.DoesNotExist:
            pass
        super(Referee, self).save(*args, **kwargs)

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

def get_upload_path(instance, filename):
    return u"referee_%s/%s" % (instance.referee.id, filename)

class Referal(models.Model):
    id = make_uuid_charfield() 
    file = models.FileField(verbose_name='Рецензия', upload_to=get_upload_path, blank=True, null=True)
    referee = models.ForeignKey(Referee, verbose_name='Учител', blank=True,
                            null=True, default='', related_name='referals',
                            on_delete=models.SET_NULL,)

    class Meta:
        app_label = "graduation_system_app"
