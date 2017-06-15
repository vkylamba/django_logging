from __future__ import absolute_import, unicode_literals
from django.apps import AppConfig
from django.conf import settings
import logging
from .queue_listner import queue_listner
from .loggers import get_logger_settings


class DjangoLoggingConfig(AppConfig):
    name = 'django_logging'
    label = 'django_logging'
    verbose_name = "Django logging"

    def ready(self):
        if not hasattr(settings, 'LOGGING') or not settings.LOGGING:
            logging_dict = get_logger_settings(
                env_name=settings.LOG_ENV_NAME,
                log_dir=settings.LOG_DIR,
                log_file_name=settings.LOG_FILE_NAME,
                application_log_level=settings.APPLICATION_LOG_LEVEL,
                logstash_listner_ip=getattr(settings, 'LOGSTASH_LISTNER_IP', None),
                logstash_listner_port=getattr(settings, 'LOGSTASH_LISTNER_PORT', None),
                logstash_tags=getattr(settings, 'LOGSTASH_TAGS', [])
            )
            logging.config.dictConfig(logging_dict)
        queue_listner.start()
