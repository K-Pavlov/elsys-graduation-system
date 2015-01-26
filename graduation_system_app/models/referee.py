# -*- coding: utf-8 -*-
import csv

from django.db import models
from django.utils.encoding import smart_bytes

from .season import Season
from .firm import Firm
from ..common.uuid_generator import make_uuid_charfield

class Referee(models.Model):
    id = make_uuid_charfield() 
    first_name = models.CharField(verbose_name='???', max_length=50)
    middle_name = models.CharField(verbose_name='???????', max_length=50, blank=True, null=True, default='')
    last_name = models.CharField(verbose_name='???????', max_length=50)
    firm = models.ForeignKey(Firm, verbose_name='????????', blank=true,
                             null=true, default='', related_name='referees',
                             on_delete=models.SET_NULL,)
    season = models.ForeignKey(Season, verbose_name='?????', blank=True,
                            null=True, default='', related_name='referees',
                            on_delete=models.SET_NULL,)

    @staticmethod
    def from_csv(csvfile):
        i = 0
        created_model = []
        reader = csv.reader(csvfile)

        for row in reader:
            first_name = row[0]
            middle_name = row[1]
            last_name = row[2]

            if (Referee.objects.filter(first_name= first_name, middle_name= middle_name,
                                       last_name= last_name).count() == 0):
                model = Referee()
                model.first_name = first_name
                model.middle_name = middle_name
                model.last_name = last_name
                firm = None

                if (len(row) > 3):
                    try:
                        firm = Firm.objects.get(name=row[3])
                    except Firm.DoesNotExist:
                        firm = Firm()
                        firm.name = row[3]
                        firm.save()
                else:
                    firm = Firm.objects.get(name=DEFAULT)

                model.firm = firm
                created_model.append(model)
 
            i += 1
            if (i % 50 == 0):
                Referee.objects.bulk_create(created_model)
                created_model = []
 
        if (created_model.count != 0):
            Referee.objects.bulk_create(created_model)

    def __str__(self):
        string = u"%s %s %s" % (self.first_name,
                                self.middle_name,
                                self.last_name)
        return smart_bytes(string)

    class Meta:
        app_label = "graduation_system_app"
