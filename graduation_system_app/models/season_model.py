# -*- coding: utf-8 -*-
from django.db import models

from season import Season
from deletable_model import DeletableModelBase, DeletableManager
from ..common.uuid_generator import make_uuid_charfield

class SeasonManager(DeletableManager):
    def get_query_set(self):
        try:
            current_season = Season.objects.get(is_active=True)
            return super(SeasonManager, self).get_query_set().filter(season=current_season)
        except Season.DoesNotExist:
            return super(SeasonManager, self).get_query_set()

class SeasonModelBase(DeletableModelBase):
    season = models.ForeignKey(Season, verbose_name='Сезон', blank=True,
                            null=True, default='', on_delete=models.SET_NULL,)
    objects = SeasonManager()

    def save(self, *args, **kwargs):
        try:
            self.season = Season.objects.get(is_active=True)
        except Season.DoesNotExist:
            pass
        super(SeasonModelBase, self).save(*args, **kwargs)

    class Meta:
       abstract = True