#!/usr/bin/env python
from __future__ import absolute_import, unicode_literals
import environ
import logging

env = environ.Env()
environ.Env.read_env()


def configure():
    from .queue_listner import queue_listner
    from .loggers import get_logger_settings
    logging_dict = get_logger_settings(
        env_name=env("LOG_ENV_NAME"),
        log_dir=env("LOG_DIR"),
        log_file_name=env("LOG_FILE_NAME"),
        application_log_level=env("APPLICATION_LOG_LEVEL", default="INFO"),
        logstash_listner_ip=env("LOGSTASH_LISTENER_IP", default=None),
        logstash_listner_port=env("LOGSTASH_LISTENER_PORT", default=None),
        logstash_tags=env.list("LOGSTASH_TAGS", default=[]),

        cloudwatch_logging_enabled=False,  # env.bool("CLOUDWATCH_LOGGING_ENABLED", default=False),
        aws_access_key_id=env("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=env("AWS_SECRET_ACCESS_KEY"),
        aws_region_name=env("AWS_REGION_NAME"),
        cloudwatch_log_group=env("CLOUDWATCH_LOG_GROUP"),
        cloud_watch_log_stream=env("CLOUD_WATCH_LOG_STREAM"),
    )
    logging.config.dictConfig(logging_dict)
    queue_listner.start()
