from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from . import Mentor

class Topic(object):
    title = models.CharField(max_length=100)
    description = models.TextField()
    mentor = models.ForeignKey(Mentor, blank=True, null=True)


