from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from graduation_system_app.models import Klass
#from system.models.supervisor import Supervisor


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    klass = models.ForeignKey(Klass, blank=True, null=True)
    topic = models.CharField(max_length=200, blank=True, null=True)
    grade = models.FloatField(
        validators=[MinValueValidator(2.0), MaxValueValidator(6.0)], blank=True, default=2.0)
    supervisor = models.ForeignKey(Supervisor, blank=True, null=True)

    def __str__(self):
            return "%s %s" % (self.first_name, self.last_name)


