import logging
import helper


main_logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                    , datefmt='%d.%m.%Y %I:%M:%S %p')

main_logger.info('I am here at main')

helper.helper_func()

# logger = logging.getLogger('helper')
#
# channel = logging.StreamHandler()
# channel.setLevel(logging.INFO)
#
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# channel.setFormatter(formatter)
#
#
# logger.addHandler(channel)
#
# helper.helper_func()
