from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Mentor(object):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


