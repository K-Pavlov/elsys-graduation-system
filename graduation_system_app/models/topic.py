# -*- coding: utf-8 -*-
import csv 

from django.db import models
from django.utils.encoding import smart_bytes
 
from .referee import Referee
from .firm import Firm
from .teacher import Teacher
from .mentor import Mentor
from .season import Season
from ..common.uuid_generator import make_uuid_charfield
 
class Topic(models.Model):
    id = make_uuid_charfield()
    title = models.CharField(verbose_name='Заглавие', max_length=100)
    description = models.TextField(verbose_name='Описание', )
    mentor = models.ForeignKey(Mentor, verbose_name='Ръководител', blank=True,
                               null=True, default='', related_name='mentors',
                               on_delete=models.SET_NULL,)
    referee = models.ForeignKey(Referee, verbose_name='Рецензент', blank=True,
                               null=True, default='', related_name='mentors',
                               on_delete=models.SET_NULL,)
    season = models.ForeignKey(Season, verbose_name='Сезон', blank=True,
                            null=True, default='', related_name='topics',
                            on_delete=models.SET_NULL,)
 
    def save(self, *args, **kwargs):
        try:
            self.season = Season.objects.get(is_active=True)
        except Season.DoesNotExist:
            pass
        super(Topic, self).save(*args, **kwargs)

    @staticmethod
    def from_csv(csvfile):
        i = 0
        created_model = []
        reader = csv.reader(csvfile)
        reader.next()

        for row in reader:
            if (Topic.objects.filter(title= row[0]).count() == 0):
                model = Topic()
                model.title = row[0]
                model.description = row[1]
                try:
                    model.season = Season.objects.get(is_active=True)
                except Season.DoesNotExist:
                    pass

                if (len(row) > 2):
                    first_name = row[2]
                    middle_name = row[3] if row[3] else ''
                    last_name = row[4]

                    mentor = None
                    try:
                        teacher = Teacher.objects.get(first_name=first_name, middle_name=middle_name, last_name=last_name)
                        try:
                            mentor = Mentor.objects.get(teacher=teacher)
                            continue 
                        except Mentor.DoesNotExist:
                            pass
                    except Teacher.DoesNotExist:
                        teacher = Teacher()
                        mentor = Mentor()

                        teacher.first_name = first_name
                        teacher.middle_name = middle_name
                        teacher.last_name = last_name

                        if(len(row) > 5):
                            firm = None
                            try:
                                firm = Firm.objects.get(name=row[5])
                            except Firm.DoesNotExist:
                                firm = Firm()
                                firm.name = row[6]
                                firm.save()

                            teacher.firm = firm
                        try:
                            teacher.season = Season.objects.get(is_active=True)
                        except Season.DoesNotExist:
                            pass

                        teacher.save()
                        mentor.teacher = teacher
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
        app_label = "graduation_system_app"