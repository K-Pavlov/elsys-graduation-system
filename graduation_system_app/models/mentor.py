# -*- coding: utf-8 -*-
import csv

from django.db import models
from django.utils.encoding import smart_bytes

from .season import Season
from .firm import Firm
from .teacher import Teacher
from ..common.uuid_generator import make_uuid_charfield

class Mentor(models.Model):
    id = make_uuid_charfield() 
    teacher = models.ForeignKey(Teacher, verbose_name='Учител', blank=True,
                            null=True, default='', related_name='mentors',
                            on_delete=models.SET_NULL,)
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
    def from_csv(csvfile):
        DEFAULT = 'ТУЕС'
        i = 0
        created_model = []
        reader = csv.reader(csvfile)
        reader.next()

        for row in reader:
            first_name = row[0]
            middle_name = row[1]
            last_name = row[2]
            model = Mentor()
            try:
               teacher = Teacher.objects.get(first_name= first_name, middle_name= middle_name,
                                       last_name= last_name)
               try:
                   Mentor.objects.get(teacher=teacher)
                   continue
               except Mentor.DoesNotExist:
                   pass
            except Teacher.DoesNotExist:
                teacher = Teacher()

                teacher.first_name = first_name
                teacher.middle_name = middle_name
                teacher.last_name = last_name

                if (len(row) > 3):
                    try:
                        firm = Firm.objects.get(name=row[3])
                    except Firm.DoesNotExist:
                        firm = Firm()
                        firm.name = row[3]
                        firm.save()
                else:
                    firm = Firm.objects.get(name=DEFAULT)

                try:
                    model.season = Season.objects.get(is_active=True)
                except Season.DoesNotExist:
                    pass
                teacher.firm = firm
                teacher.save()

            try:
                teacher.season = Season.objects.get(is_active=True)
            except Season.DoesNotExist:
                pass

            model.teacher = teacher
            created_model.append(model)
            i += 1
            if (i % 50 == 0):
                Mentor.objects.bulk_create(created_model)
                created_model = []
 
        if (created_model.count != 0):
            Mentor.objects.bulk_create(created_model)

    def __str__(self):
        return self.teacher.__str__()

    class Meta:
        app_label = "graduation_system_app"