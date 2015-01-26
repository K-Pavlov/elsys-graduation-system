# -*- coding: utf-8 -*-
import csv

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .referee import Referee
from .mentor import Mentor
from .topic import Topic
from .season import Season 
from ..common.uuid_generator import make_uuid_charfield

class Student(models.Model):
    # change to db realtion
    ClassLetters = (
        ('А', 'А'),
        ('Б', 'Б'),
        ('В', 'В'),
        ('Г', 'Г')
    )

    Specialization = (
        ('software', u'Софтуерно инженерство'),
        ('computer_networks', u'Компютърни мрежи'),
        ('hardware', u'Компютърна техника и технологии')
    )

    id = make_uuid_charfield()
    first_name = models.CharField(verbose_name='Име', max_length=50)
    middle_name = models.CharField(verbose_name='Презиме', max_length=50,
                                   blank=True, null=True, default='')
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    class_letter = models.CharField(verbose_name='Клас', max_length=1, blank=True,
                                    null=True, default='',choices=ClassLetters)
    specialization = models.CharField(verbose_name='Специалност', max_length=150,
                                      blank=True, null=True, default='',
                                      choices=Specialization)
    grade = models.FloatField(verbose_name='Оценка', blank=True, default=2.0,
                              validators=[MinValueValidator(2.0), MaxValueValidator(6.0)],)
    topic = models.ForeignKey(Topic, verbose_name='Тема', blank=True, null=True,
                              related_name='students', default='',
                              on_delete=models.SET_NULL,)
    mentor = models.ForeignKey(Mentor, verbose_name='Дипломен ръководител', blank=True,
                               null=True, default='', related_name='students',
                               on_delete=models.SET_NULL,)
    season = models.ForeignKey(Season, verbose_name='Сезон', blank=True,
                            null=True, default='', related_name='students',
                            on_delete=models.SET_NULL,)
    referee = models.ForeignKey(Referee, verbose_name='Рецензент', blank=True, null=True,
                              related_name='students', default='',
                              on_delete=models.SET_NULL,)

    def __str__(self):
            return u"%s %s %s" % (self.first_name, self.middle_name, self.last_name)

    @staticmethod
    def from_csv(csvfile):
        i = 0
        created_model = []
        reader = csv.reader(csvfile)

        for row in reader:
            first_name = row[0]
            middle_name = row[1]
            last_name = row[2]

            if (Student.objects.filter(first_name= first_name, middle_name= middle_name,
                                       last_name= last_name).count() == 0):
                model = Student()
                model.first_name = first_name
                model.middle_name = middle_name
                model.last_name = last_name
                model.class_letter = row[3]
                model.specialization = row[4]

                if (len(row) > 5):
                    try:
                        model.topic = Topic.objects.get(title= row[5])
                    except Topic.DoesNotExist:
                        pass

                if(len(row) > 6):
                    try: 
                        model.mentor = Mentor.objects.get(first_name= row[6], middle_name= row[7], last_name= row[8])
                    except Mentor.DoesNotExist:
                        pass

                created_model.append(model)
 
            i += 1
            if (i % 50 == 0):
                Student.objects.bulk_create(created_model)
                created_model = []
 
        if (created_model.count != 0):
            Student.objects.bulk_create(created_model)

    class Meta:
        app_label = "graduation_system_app"


