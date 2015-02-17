import uuid

from django.db import models

def make_uuid_charfield():
    return models.CharField(max_length=36, primary_key=True, default=make_uuid)

def make_uuid():
    return str(uuid.uuid4())
