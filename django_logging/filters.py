import logging
import datetime


class TimestampFilter(logging.Filter):
    """
        Custom timestamp filter for logging.
    """

    def filter(self, record):
        time_now = datetime.datetime.utcnow()
        record.timestamp = time_now.isoformat() + "+00:00"
        return True


class ExecpathFilter(logging.Filter):
    """
        Custom ExecpathFilter filter for logging.
        To be used with default handler only.
    """

    def filter(self, record):
        if record.funcName == 'handle_uncaught_exception':
            exc_info = record.exc_info
            if len(exc_info) > 2:
                current_tb = exc_info[2]
                last_tb = None
                while current_tb != None:
                    last_tb = current_tb
                    current_tb = current_tb.tb_next
                if last_tb:
                    record.execpath = last_tb.tb_frame.f_code.co_filename
                    record.execline = last_tb.tb_lineno
                    if record.exc_text:
                        msg_list = record.exc_text.split('\n')
                        record.execmsg = msg_list[-1].strip()
                    else:
                        record.execmsg = exc_info[0].__doc__
                        record.exc_text = 'IGNORE: ' + str(record.execmsg) if record.execmsg else ''
                    return True
        return False
