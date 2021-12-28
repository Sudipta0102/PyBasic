# if I want a start afresh every time I run this script then. then need to use filemode arg.

import logging

logging.basicConfig(filename='../example2.log', filemode='w', encoding='utf-8', level=logging.DEBUG)

logging.debug('this is a debug message')
logging.info('this is an info message')
logging.warning('this is a warning message')
logging.error('this is an error message')
logging.critical('this is a critical message')