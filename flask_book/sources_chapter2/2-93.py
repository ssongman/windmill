import logging
from logging.handlers import SysLogHandler

logger = logging.getLogger('syslogger')

handler = SysLogHandler(address='/dev/log')

formatter = logging.Formatter('%(name)s: %(levelname)s %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)