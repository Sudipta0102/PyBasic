import logging


main_logger = logging.getLogger('main')

logging.basicConfig(format='%(asctime)s   %(levelname)s : %(message)s',
                    level=logging.DEBUG, datefmt='%d.%m.%Y %I:%M:%S %p')



