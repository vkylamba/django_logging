from queue import Queue
from logging.handlers import QueueListener
from django.conf import settings

log_queue_size = getattr(settings, 'LOG_HANDLER_QUEUE_SIZE', 10000)

# Log queue used by queue handler
log_queue = Queue(maxsize=log_queue_size)

queue_listner = QueueListener(
    log_queue,
    # console_handler,
    # mail_admins_handler,
    # file_handler,
    # socket_handler
)
