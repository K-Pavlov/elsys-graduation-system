from django.db import models
from graduation_system_app.common.uuid_generator import make_uuid_charfield

class Klass(models.Model):
    id = make_uuid_charfield()
    classLetter = models.CharField(max_length=1)
    specialization = models.CharField(max_length=30)
    """description of class"""

    class Meta:
        app_label = "graduation_system_app"


