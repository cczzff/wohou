# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 05:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_todo_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='already_remid',
            field=models.BooleanField(default=False, verbose_name='\u5df2\u7ecf\u63d0\u9192\u8fc7'),
        ),
    ]
