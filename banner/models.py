# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Banner(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField('banner标题', max_length=100, blank=True, default='')
    picture_url = models.CharField('图片地址', max_length=100, blank=True, default='')
    is_use = models.BooleanField('是否有效', default=False)

    class Meta:
        ordering = ('created',)
        db_table = 'banner'

    def __unicode__(self):  # __unicode__ on Python 2
        return self.title
