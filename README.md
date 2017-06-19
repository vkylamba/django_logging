# Async Django Logger

## Install Django Logging.
1. `pip install git+https://github.com/Gale43/django_logging.git`


2. Add Django Logging to Installed Apps
```
INSTALLED_APPS = [
    ...
    django_logging
]
```


3. Add the following settings in your Settings.py
```
LOG_ENV_NAME = env("LOG_ENV_NAME", default="mackenzie-dev")
LOG_DIR = env("LOG_DIR", default="/app/logs")
LOG_FILE_NAME = env("LOG_FILE_NAME", default='django.log')
APPLICATION_LOG_LEVEL = env("APPLICATION_LOG_LEVEL", default="DEBUG")
LOGSTASH_LISTNER_IP = env("LOGSTASH_LISTNER_IP", default=None)
LOGSTASH_LISTNER_PORT = env("LOGSTASH_LISTNER_PORT", default=None)
LOGSTASH_TAGS = []
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
