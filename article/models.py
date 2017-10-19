# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from account.models import Account


class Article(models.Model):
    account = models.ForeignKey(Account)
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('created',)
        db_table = 'article'
