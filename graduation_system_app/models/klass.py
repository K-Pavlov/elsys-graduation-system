from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Klass(models.Model):
    classLetter = models.CharField(max_length=1)
    specialization = models.CharField(max_length=30)
    """description of class"""


