# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class CityInfo(models.Model):
    cityid = models.IntegerField('城市id', default=0)
    city = models.CharField('城市名', max_length=100, blank=True, default='')
    citycode = models.CharField('城市编码', max_length=100, blank=True, default='')
    parentid = models.IntegerField('父城市id', default=0)

    class Meta:
        db_table = 'city_info'

    def __unicode__(self):  # __unicode__ on Python 2
        return self.city


class StarInfo(models.Model):

    astroid = models.IntegerField('星座id', default=0)
    astroname = models.CharField('星座名称', max_length=100, blank=True, default='')
    date = models.CharField('星座日期', max_length=100, blank=True, default='')
    pic = models.CharField('星座图片url', max_length=100, blank=True, default='')

    class Meta:
        db_table = 'star_info'

    def __unicode__(self):  # __unicode__ on Python 2
        return self.astroname
