from __future__ import absolute_import, unicode_literals
from django.apps import AppConfig
from .queue_listner import queue_listner


class DjangoLoggingConfig(AppConfig):
    name = 'django_logging'
    label = 'django_logging'
    verbose_name = "Django logging"

    def ready(self):
        queue_listner.start()
