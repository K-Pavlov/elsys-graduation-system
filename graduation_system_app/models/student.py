from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .klass import Klass
from .mentor import Mentor
from .topic import Topic
from graduation_system_app.common.uuid_generator import make_uuid_charfield

class Student(models.Model):
    id = make_uuid_charfield()
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    klass = models.ForeignKey(Klass, blank=True, null=True)
    topic = models.ForeignKey(Topic, blank=True, null=True)
    mentor = models.ForeignKey(Mentor, blank=True, null=True)
    grade = models.FloatField(
        validators=[MinValueValidator(2.0), MaxValueValidator(6.0)], blank=True, default=2.0)

    def __str__(self):
            return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        app_label = "graduation_system_app"


