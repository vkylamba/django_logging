# Async Django Logger

[![Requirements Status](https://requires.io/github/Gale43/django_logging/requirements.svg?branch=master)](https://requires.io/github/Gale43/django_logging/requirements/?branch=master)
[![Travis-CI Status](https://travis-ci.org/Gale43/django_logging.svg?branch=master)](https://travis-ci.org/Gale43/django_logging)
[![Coverage Status](https://coveralls.io/repos/github/Gale43/django_logging/badge.svg?branch=master)](https://coveralls.io/github/Gale43/django_logging?branch=master)
[![Sonarcloud Status](https://sonarcloud.io/api/badges/gate?key=gale43.django_logging)](https://sonarcloud.io/dashboard?id=gale43.django_logging)


## Install Django Logging.
1. `pip install git+https://github.com/Gale43/django_logging.git`


2. Add Django Logging to Installed Apps
```
INSTALLED_APPS = [
    ...
    'django_logging',
]
```


3. Add the following settings in your Settings.py
```
# The current environment name.
LOG_ENV_NAME = env("LOG_ENV_NAME", default="project-dev")
# The directory containing the log file.
LOG_DIR = env("LOG_DIR", default="/app/logs")
# Name of the log file
LOG_FILE_NAME = env("LOG_FILE_NAME", default='django.log')
# Logging Level. Choose from INFO, DEBUG, WARNING, ERROR or CRITICAL
APPLICATION_LOG_LEVEL = env("APPLICATION_LOG_LEVEL", default="DEBUG")

# Logstash settings
# Logstash IP.
LOGSTASH_LISTENER_IP = env("LOGSTASH_LISTNER_IP", default=None)
# Logstash Port.
LOGSTASH_LISTENER_PORT = env("LOGSTASH_LISTNER_PORT", default=None)
# List of Logstash tags.
LOGSTASH_TAGS = []

# AWS cloudwatch settings
CLOUDWATCH_LOGGING_ENBLED = env('CLOUDWATCH_LOGGING_ENBLED', default=False)
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID', default='AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY', default='AWS_SECRET_ACCESS_KEY')
AWS_REGION_NAME = env('AWS_REGION_NAME', default='AWS_REGION_NAME')
CLOUDWATCH_LOG_GROUP = env('CLOUDWATCH_LOG_GROUP', default='CLOUDWATCH_LOG_GROUP')
CLOUD_WATCH_LOG_STREAM = env('CLOUD_WATCH_LOG_STREAM', default='CLOUD_WATCH_LOG_STREAM')
```


## Usage
```
import logging
logger = logging.getLogger('application')

# All logging methods are available
logger.debug()
logger.info()
logger.warning()
logger.error()
logger.critical()
logger.log()
logger.exception()
```

Logs would be printed to the `console` as well as the file `LOG_DIR/LOG_FILE_NAME`
