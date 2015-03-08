# -*- coding: utf-8 -*-
import csv 

from django.db import models
from django.utils.encoding import smart_bytes
 
from mentor import Mentor
from shared.models.firm import Firm
from shared.models.season import Season
from shared.models.season_model import SeasonModelBase
from shared.models.teacher import Teacher
from reviewing.models import Referee
 
class Topic(SeasonModelBase):
    title = models.CharField(verbose_name='Заглавие', max_length=100)
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

    @staticmethod
    def create_from_upload(objects):
        i = 0
        created_model = []

        for topic in objects:
            if (Topic.objects.filter(title= topic['title']).count() == 0):
                model = Topic()
                try:
                    model.title = topic['title']
                except KeyError:
                    model.title = ''
                try:
                    model.description = topic['description']
                except KeyError:
                    model.description = ''

                try:
                    model.season = Season.objects.get(is_active=True)
                except Season.DoesNotExist:
                    pass

                mentor = Mentor.create(topic)

                if(mentor):
                    mentor.save()
                    model.mentor = mentor

                try:
                    model.season = Season.objects.get(is_active=True)
                except Season.DoesNotExist:
                    pass
                created_model.append(model)
 
            i += 1
            if (i % 50 == 0):
                Topic.objects.bulk_create(created_model)
                created_model = []
 
        if (created_model.count != 0):
            Topic.objects.bulk_create(created_model)
 
    def __str__(self):
        string = u"%s" % self.title
        return smart_bytes(string)
 
    class Meta:
        app_label = 'division'
        db_table = 'topic'
        ordering = ['title']