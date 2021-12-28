import logging

logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.DEBUG)


logging.debug('this is a debug message')
logging.info('this is an info message')
logging.warning('this is a warning message')
logging.error('this is an error message')
logging.critical('this is a critical message')

# 1. see 'root' from console is gone now because of setting format.
# 2. also this mevelname and message are both attributes, I need to refer this:
# https://docs.python.org/3/library/logging.html#logrecord-attributes


