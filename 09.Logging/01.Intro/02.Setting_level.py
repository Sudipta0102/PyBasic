# I can remedy the prior problem by setting levels at basicconfig()
import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug('this is a debug message')
logging.info('this is an info message')
logging.warning('this is a warning message')
logging.error('this is an error message')
logging.critical('this is a critical message')

# now everything gets printed.

