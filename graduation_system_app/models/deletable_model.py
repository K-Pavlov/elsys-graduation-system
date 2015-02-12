# -*- coding: utf-8 -*-
from django.db import models

from ..common.uuid_generator import make_uuid_charfield

class DeletableQuerySet(models.query.QuerySet):
    def delete(self):
        return super(DeletableQuerySet, self).update(is_deleted=True)

class DeletableManager(models.Manager):
    def get_query_set(self):
        return DeletableQuerySet(self.model).filter(is_deleted=False)

class DeletableModelBase(models.Model):
    id = make_uuid_charfield()
    is_deleted = models.BooleanField(verbose_name='Изтрит', default=False)
    objects = DeletableManager()

    def delete(self):
        self.is_deleted = True
        self.save()

    class Meta:
       abstract = True