# -*- coding: utf-8 -*-
import csv

from django.db import models
from django.utils.encoding import smart_bytes

from season_model import SeasonModelBase
from season import Season
from firm import Firm
from teacher import Teacher

class Comission(SeasonModelBase):
    members_of_comission = models.ManyToManyField(Teacher, verbose_name='Членове на комисията', blank=True,
                            null=True, default='', related_name='members_of_comission',)
    start_time = models.DateTimeField(auto_now_add=False, blank=True, null=True, default='', verbose_name='Начален час')
    head_of_comission = models.OneToOneField(Teacher, verbose_name='Председател на комисията', blank=True,
                            null=True, default='', related_name='head_of_comission',
                            on_delete=models.SET_NULL,)

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

            if (Teacher.objects.filter(first_name= first_name, middle_name= middle_name,
                                       last_name= last_name).count() == 0):
                model = Comission()
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

                teacher.firm = firm
                teacher.save()
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