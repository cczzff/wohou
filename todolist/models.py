# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# # Create your models here.
from account.models import Account


class Todo(models.Model):
    title = models.CharField('todo标题', max_length=100)
    todo_time = models.DateTimeField(blank=False)
    note = models.CharField('备注', max_length=200, blank=True, default='')
    sms_remid = models.BooleanField('短信提醒', default=False)
    created = models.DateTimeField(auto_now_add=True)
    # related_name 用于反向查询
    account = models.ForeignKey(Account, related_name='strategy')

    class Meta:
        ordering = ('created',)
        db_table = 'todo'

    def __unicode__(self):  # __unicode__ on Python 2
        return self.title

