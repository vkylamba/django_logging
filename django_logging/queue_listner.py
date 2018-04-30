from queue import Queue
from logging.handlers import QueueListener
import environ

env = environ.Env()
environ.Env.read_env()
log_queue_size = env('LOG_HANDLER_QUEUE_SIZE', default=10000)

# Log queue used by queue handler
log_queue = Queue(maxsize=int(log_queue_size))

queue_listner = QueueListener(
    log_queue
)
