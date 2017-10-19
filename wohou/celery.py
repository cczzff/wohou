# coding=utf8

from __future__ import absolute_import
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
from wohou import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wohou.settings')

app = Celery('wohou', broker="redis://localhost")

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings)
