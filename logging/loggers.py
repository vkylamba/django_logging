import logging
from django.utils.log import AdminEmailHandler, RequireDebugTrue, RequireDebugFalse
from logging.handlers import RotatingFileHandler
from logging import StreamHandler

from .filters import TimestampFilter, ExecpathFilter
from .logstash_handler import SocketLogstashHandler
from .apps import log_queue
from .queue_listner import queue_listner


def get_logger_settings(env_name, log_dir, log_file_name, application_log_level='DEBUG',
                        logstash_listner_ip=None,
                        logstash_listner_port=None,
                        logstash_tags=[]
                        ):

    # Formatters
    verbose_formatter = logging.Formatter(
        '[%(timestamp)s] [{env_name}] [%(levelname)s] [%(pathname)s:%(lineno)d] %(message)s'.format(env_name=env_name),
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    console_handler = StreamHandler()
    console_handler.addFilter(RequireDebugTrue())
    console_handler.addFilter(TimestampFilter())
    console_handler.setFormatter(verbose_formatter)

    mail_admins_handler = AdminEmailHandler()
    mail_admins_handler.include_html = True
    mail_admins_handler.setLevel(logging.ERROR)
    mail_admins_handler.addFilter(RequireDebugFalse())
    mail_admins_handler.addFilter(TimestampFilter())
    mail_admins_handler.setFormatter(verbose_formatter)

    file_handler = RotatingFileHandler(
        filename=log_dir + '/' + log_file_name,
        maxBytes=20 * 1024 * 1024,
        backupCount=7
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.addFilter(TimestampFilter())
    file_handler.setFormatter(verbose_formatter)

    socket_handler = None
    if logstash_listner_ip is not None and logstash_listner_port is not None:
        socket_handler = SocketLogstashHandler(logstash_listner_ip, logstash_listner_port)
        socket_handler.setLevel(logging.ERROR)
        socket_handler.addFilter(RequireDebugTrue())
        socket_handler.addFilter(TimestampFilter())
        socket_handler.setFormatter(verbose_formatter)
        socket_handler.tags = logstash_tags

    logging_dict = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            },
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue'
            },
            'execpath': {
                '()': ExecpathFilter,
            },
            'timestamp': {
                '()': TimestampFilter,
            },
        },
        'formatters': {
            'simple': {
                'format': '[%(asctime)s] %(levelname)s %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
            'verbose': {
                'format': '[%(timestamp)s] [{env_name}] [%(levelname)s] [%(pathname)s:%(lineno)d] %(message)s'.format(env_name=env_name),
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
            'default': {
                # To be used with default handler only.
                'format': '[%(timestamp)s] [{env_name}] [%(levelname)s] [%(execpath)s:%(execline)d] %(execmsg)s'.format(env_name=env_name),
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
        },
        'handlers': {
            'default': {
                'level': 'DEBUG',
                'filters': ['timestamp', 'execpath'],
                'class': 'logging.FileHandler',
                'filename': log_dir + '/' + log_file_name,
                'formatter': 'default'
            },
            'console': {
                'filters': ['require_debug_true', 'timestamp'],
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            },
            'mail_admins': {
                'filters': ['require_debug_false', ],
                'class': 'django.utils.log.AdminEmailHandler',
                'include_html': True,
                'level': 'ERROR',
            },
            'file_error': {
                'class': 'logging.FileHandler',
                'filters': ['timestamp'],
                'filename': log_dir + '/' + log_file_name,
                'formatter': 'verbose',
            },
            'queue_handler': {
                'class': 'logging.handlers.QueueHandler',
                'filters': ['timestamp'],
                'formatter': 'verbose',
                'queue': log_queue
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['default', 'mail_admins', ],
                'level': 'ERROR',
                'propagate': True
            },
            'django.security.DisallowedHost': {
                'level': 'ERROR',
                'handlers': ['file_error', 'console', 'mail_admins', ],
                'propagate': True
            },
            'application': {
                'handlers': ['queue_handler'],
                'level': application_log_level,
                'propagate': True
            },
        },
    }

    queue_listner.handlers = [
        console_handler,
        mail_admins_handler,
        file_handler
    ]
    if socket_handler:
        queue_listner.handlers.append(socket_handler)

    return logging_dict
