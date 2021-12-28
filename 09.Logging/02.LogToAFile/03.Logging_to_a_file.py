import logging

logging.basicConfig(filename='../example1.log', encoding='utf-8', level=logging.DEBUG)

logging.debug('this is a debug message')
logging.info('this is an info message')
logging.warning('this is a warning message')
logging.error('this is an error message')
logging.critical('this is a critical message')


# If I run this multiple times, then it will append this again and again.
