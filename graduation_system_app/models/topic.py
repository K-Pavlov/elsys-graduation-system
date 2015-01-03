from django.db import models
from graduation_system_app.common.uuid_generator import make_uuid_charfield

class Topic(models.Model):
    id = make_uuid_charfield()
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        app_label = "graduation_system_app"


