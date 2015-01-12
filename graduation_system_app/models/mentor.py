# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import smart_bytes

from ..common.uuid_generator import make_uuid_charfield

class Mentor(models.Model):
    id = make_uuid_charfield() 
    first_name = models.CharField(verbose_name='Име', max_length=50)
    middle_name = models.CharField(verbose_name='Презиме', max_length=50, blank=True, null=True, default='')
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)

    @staticmethod
    def from_csv(csvfile_path):
        i = 0
        created_model = []

        with open(csvfile_path) as csv_file:
            rows = [row for row in csv.reader(csv_file, encoding='utf-8')]
            for row in rows:
                if(not already_exists(row[0], row[1], row[2])):
                    model = Mentor()
                    model.first_name = row[0]
                    model.middle_name = row[1]
                    model.last_name = row[2]
                    created_model.append(model)

                i += 1
                if i % 50 == 0:
                    Mentor.objects.bulk_create(created_model)
                    created_model = []

            if created_model.count != 0:
                Mentor.objects.bulk_create(created_model)

    @staticmethod
    def already_exists(values):
        return Mentor.objects.filter(first_name= values[0], middle_name= values[1],
                                     last_name= values[2]).count() > 0

    def __str__(self):
        string = u"%s %s %s" % (self.first_name,
                                self.middle_name,
                                self.last_name)
        return smart_bytes(string)

    class Meta:
        app_label = "graduation_system_app"
