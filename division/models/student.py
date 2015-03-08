# -*- coding: utf-8 -*-
import csv

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.encoding import smart_bytes

from defences.models import Comission
from specialization import Specialization
from class_letter import ClassLetter
from mentor import Mentor
from topic import Topic
from shared.models.season_model import SeasonModelBase
from shared.models.teacher import Teacher
from shared.models.season import Season 
from reviewing.models import Referee

class Student(SeasonModelBase):
    first_name = models.CharField(verbose_name='Име', max_length=50)
    middle_name = models.CharField(verbose_name='Презиме', max_length=50,
                                   blank=True, null=True, default='')
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    grade = models.FloatField(verbose_name='Оценка', blank=True, default=2.0,
                              validators=[MinValueValidator(2.0), MaxValueValidator(6.0)],)
    class_letter = models.ForeignKey(ClassLetter, verbose_name='Паралелка', blank=True, null=True,
                              related_name='students', default='',
                              on_delete=models.SET_NULL,)
    specialization = models.ForeignKey(Specialization, verbose_name='Специалност', blank=True, null=True,
                              related_name='students', default='',
                              on_delete=models.SET_NULL,)
    topic = models.ForeignKey(Topic, verbose_name='Тема', blank=True, null=True,
                              related_name='students', default='',
                              on_delete=models.SET_NULL,)
    mentor = models.ForeignKey(Mentor, verbose_name='Дипломен ръководител', blank=True,
                               null=True, default='', related_name='students',
                               on_delete=models.SET_NULL,)
    comission = models.ForeignKey(Comission, verbose_name='Комисия', blank=True,
                            null=True, default='', related_name='students',
                            on_delete=models.SET_NULL,)
    referee = models.ForeignKey(Referee, verbose_name='Рецензент', blank=True, null=True,
                              related_name='students', default='',
                              on_delete=models.SET_NULL,)

    def soft_delete(self):
        self.referee = None
        self.mentor = None
        self.comission = None
        self.topic = None
        self.specialization = None
        self.class_letter = None

        return super(Student, self).soft_delete()

    def __str__(self):
            return smart_bytes(u"%s %s %s" % (self.first_name, self.middle_name, self.last_name))

    @staticmethod
    def __check_names(item_dict, fname, mname, lname):
        try:
            first_name = item_dict[fname]
            if(not first_name): 
                return False
        except KeyError:
            return False
        try:
            middle_name = item_dict[mname]
        except KeyError:
            middle_name = ''
        try: 
            last_name = item_dict[lname]
            if(not last_name):
                return False
        except KeyError:
            return False

        return {
            'fname': first_name,
            'mname': middle_name,
            'lname': last_name,
        }

    @staticmethod
    def __get_class_letter_spec(model, student_dict):
        try:
            letter = student_dict['class-letter']
            try:
                model.class_letter = ClassLetter.objects.get(letter=letter)
            except ClassLetter.DoesNotExist:
                class_letter = ClassLetter()
                class_letter.letter = letter
                class_letter.save()
                model.class_letter = class_letter
        except KeyError:
            pass
        
        try:
            spec = student_dict['spec']
            try:
                model.specialization = Specialization.objects.get(name=spec)
            except Specialization.DoesNotExist:
                specialization = Specialization()
                specialization.name = spec
                specialization.save()
                model.specialization = specialization
        except KeyError:
            pass

    @staticmethod
    def __get_mentor(model, student_dict):
        try:
            fname = student_dict['fname-mentor']
            lname = student_dict['lname-mentor']
            mname = None
            firm = None
            try:
                mname = student_dict['mname-mentor']
                firm = student_dict['firm']
            except KeyError:
                pass
        
            mentor_dict = {
                'fname': fname,
                'mname': mname,
                'lname': lname
            }
        
            if(firm):
                mentor_dict['firm'] = firm
        
            mentor = Mentor.create(mentor_dict)
            mentor.save()
            model.mentor = mentor
        except KeyError:
            pass

    @staticmethod
    def __get_topic(model, student_dict):
        try:
            topic = student_dict['topic']
            try:
                model.topic = Topic.objects.get(title=topic)
                try:
                    model.topic.mentor = model.mentor
                    model.topic.save()
                except Mentor.DoesNotExist:
                    pass
            except Topic.DoesNotExist:
                pass
        except KeyError:
            pass

    @staticmethod
    def create_from_upload(objects):
        i = 0
        created_model = []
        print 'wtf'
        for student_dict in objects:
            student_names = Student.__check_names(student_dict, 'fname', 'mname', 'lname')
            if(student_names):
                first_name = student_names['fname']
                middle_name = student_names['mname']
                last_name = student_names['lname']
            else:
                continue

            if (Student.objects.filter(first_name= first_name, middle_name= middle_name,
                                       last_name= last_name).count() == 0):
                model = Student()
                model.first_name = first_name
                model.middle_name = middle_name
                model.last_name = last_name
                
                Student.__get_class_letter_spec(model, student_dict)
                Student.__get_mentor(model, student_dict)
                Student.__get_topic(model, student_dict)

                try:
                    model.season = Season.objects.get(is_active=True)
                except Season.DoesNotExist:
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
        db_table = "student"