import logging.handlers
handler = logging.handlers.RotatingFileHandler(filename, mode='a', maxBytes=10485760, backupCount=5, encoding='utf-8', delay=False)