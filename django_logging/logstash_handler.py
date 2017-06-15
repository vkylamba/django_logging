from logging.handlers import SocketHandler
from logstash import formatter
import json


class SocketLogstashHandler(SocketHandler):
    """
        Socket based logstash handler.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def emit(self, record):
        record.msg = self.format(record) + '\n'
        logstash_formatter = formatter.LogstashFormatterVersion1(
            'logstash',
            getattr(self, 'tags', []),
            getattr(self, 'fqdn', False)
        )

        message = logstash_formatter.format(record)
        message_string = message.decode()
        message_dict = json.loads(message_string)
        message_dict['type'] = 'django_log'
        message = json.dumps(message_dict) + '\n'
        if self.sock is None:
            self.sock = self.makeSocket()
        try:
            self.sock.send(message.encode())
        except Exception as e:
            print(e)
