# -*- coding: utf-8 -*-
import csv

from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import smart_bytes

from shared.models.model_creator import create_mentor_referee
from shared.models.deletable_model import DeletableModelBase, DeletableManager
from shared.models.season import Season
from shared.models.firm import Firm
from shared.models.teacher import Teacher
from shared.models.season_model import SeasonModelBase

class Referee(SeasonModelBase):
    teacher = models.ForeignKey(Teacher, verbose_name='Учител', blank=True,
                            null=True, default='', related_name='referees',)
    email = models.EmailField(verbose_name='Имейл', max_length=254, blank=True,
                              null=True, default='')

    def soft_delete(self):
        self.topics.clear()
        self.students.clear()

        return super(Referee, self).soft_delete()

    def validate_unique(self, *args, **kwargs):
        super(Referee, self).validate_unique(*args, **kwargs)
        if(not self.id):
            if(self.__class__.objects.filter(teacher=self.teacher, season=self.season).exists()):
                raise ValidationError(
                    {
                        NON_FIELD_ERRORS:
                        ('Рецензент със същите имена вече съществува в този сеноз',)
                    }
                )

            if(self.__class__.objects.filter(email=self.email)):
                raise ValidationError(
                    {
                        NON_FIELD_ERRORS:
                        ('Рецензент със същия имейл вече съществува')
                    }
                )

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

            if(i % 50 == 0):
                Referee.objects.bulk_create(created_model)
                created_model = []
 
        if(created_model.count != 0):
            Referee.objects.bulk_create(created_model)

    @staticmethod
    def create(referee_dict):
        return create_mentor_referee(Referee, referee_dict)

    def __str__(self):
        return self.teacher.__str__()

    class Meta:
        app_label = 'reviewing'
        db_table = 'referee'
        ordering = ['teacher']

def _get_upload_path(instance, filename):
    return u'referee_%s/%s' % (instance.referee.id, filename)

class Referal(DeletableModelBase):
    file = models.FileField(verbose_name='Рецензия', upload_to=_get_upload_path, blank=True, null=True)
    referee = models.ForeignKey(Referee, verbose_name='Рецензент', blank=True,
                            null=True, default='', related_name='referals',
                            on_delete=models.SET_NULL,)
    def soft_delete(self):
        self.referee = None

        return super(Referal, self).soft_delete()

    class Meta:
        app_label = 'reviewing'
        db_table = 'referal'
        ordering = ['referee']