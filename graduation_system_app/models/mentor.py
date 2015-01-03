from django.db import models

from graduation_system_app.common.uuid_generator import make_uuid_charfield

class Mentor(models.Model):
    id = make_uuid_charfield() 
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)

    @staticmethod
    def from_csv(csvfile):
        pass

    class Meta:
        app_label = "graduation_system_app"
