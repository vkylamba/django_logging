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
                logstash_listner_ip=getattr(settings, 'LOGSTASH_LISTENER_IP', None),
                logstash_listner_port=getattr(settings, 'LOGSTASH_LISTENER_PORT', None),
                logstash_tags=getattr(settings, 'LOGSTASH_TAGS', []),
                cloudwatch_logging_enabled=getattr(settings, "CLOUDWATCH_LOGGING_ENABLED", False),
                aws_access_key_id=getattr(settings, "AWS_ACCESS_KEY_ID", None),
                aws_secret_access_key=getattr(settings, "AWS_SECRET_ACCESS_KEY", None),
                aws_region_name=getattr(settings, "AWS_REGION_NAME", None),
                cloudwatch_log_group=getattr(settings, "CLOUDWATCH_LOG_GROUP", None),
                cloud_watch_log_stream=getattr(settings, "CLOUD_WATCH_LOG_STREAM", None),
                sentry_logging_enabled=getattr(settings, "SENTRY_ENABLED", False),
                console_debug_filter_enabled=getattr(settings, "CONSOLE_DEBUG_FILTER_ENABLED", True),
            )
            logging.config.dictConfig(logging_dict)
        queue_listner.start()
