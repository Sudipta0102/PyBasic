import logging

helper_logger = logging.getLogger(__name__)


class HelperClass:
    def __init__(self, val1: int, val2: int):
        self.logger = logging.getLogger('parentmodule.childmodule.helper.HelperClass')
        self.logger.info('Instance is being created')
        self.val1 = val1
        self.val2 = val2

    def cal_sum(self):
        self.logger.info('sum func called')
        sum = self.val1 + self.val2
        self.logger.info('sum done')


def any_func():
    helper_logger.info("received a call to 'cal_sum'")


