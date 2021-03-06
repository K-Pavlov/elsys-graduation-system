# -*- coding: utf-8 -*-
import csv 

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.encoding import smart_bytes
 
from mentor import Mentor
from shared.models.firm import Firm
from shared.models.season import Season
from shared.models.season_model import SeasonModelBase
from shared.models.teacher import Teacher
from reviewing.models import Referee
 
class Topic(SeasonModelBase):
    title = models.CharField(verbose_name='Заглавие', max_length=100,)
    description = models.TextField(verbose_name='Описание',)
    mentor = models.ForeignKey(Mentor, verbose_name='Ръководител', blank=True,
                               null=True, default='', related_name='topics',
                               on_delete=models.SET_NULL,)
    referee = models.ForeignKey(Referee, verbose_name='Рецензент', blank=True,
                               null=True, default='', related_name='topics',
                               on_delete=models.SET_NULL,)

    def soft_delete(self):
        self.students.clear()
        self.mentor = None
        self.referee = None

        return super(Topic, self).soft_delete()

    def validate_unique(self, *args, **kwargs):
        super(Topic, self).validate_unique(*args, **kwargs)
        if(self.pk is not None):
            if(self.__class__.objects.filter(title=self.title, season=self.season).exists()):
                raise ValidationError(
                    {
                        'title': ('Тема със същото заглавие вече същетсвува в този сезон',)
                    }
                )

    @staticmethod
    def create_from_upload(objects):
        i = 0
        created_model = []

        for topic_dict in objects:
            if (Topic.objects.filter(title= topic_dict['title']).count() == 0):
                model = Topic()
                try:
                    model.title = topic_dict['title']
                except KeyError:
                    model.title = ''
                try:
                    model.description = topic_dict['description']
                except KeyError:
                    model.description = ''

                try:
                    model.season = Season.objects.get(is_active=True)
                except Season.DoesNotExist:
                    pass

                mentor = Mentor.create(topic_dict)

                if(mentor):
                    mentor.save()
                    model.mentor = mentor

                try:
                    model.season = Season.objects.get(is_active=True)
                except Season.DoesNotExist:
                    pass
                created_model.append(model)
 
            i += 1
            if(i % 50 == 0):
                Topic.objects.bulk_create(created_model)
                created_model = []
 
        if(created_model.count != 0):
            Topic.objects.bulk_create(created_model)
 
    def __str__(self):
        string = u"%s" % self.title
        return smart_bytes(string)
 
    class Meta:
        app_label = 'division'
        db_table = 'topic'
        ordering = ['title']