# coding=utf-8
"""
Python记录日志
"""
import logging
import time

rq = time.strftime('%Y%m%d', time.localtime(time.time()))


class BaseLog(object):
    def __init__(self, name):
        self.path = '/data/log/'
        self.name = name
        self.filename = name + rq + '.log'
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.INFO)
        self.fh = logging.FileHandler(self.path + self.filename)
        self.fh.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s')
        self.fh.setFormatter(self.formatter)
        self.logger.addHandler(self.fh)

    def info(self, msg):
        msg = self._get_msg_info(msg)
        self.logger.info(msg)

    def warning(self, msg):
        msg = self._get_msg_info(msg)
        self.logger.warning(msg)

    def error(self, msg):
        msg = self._get_msg_info(msg)
        self.logger.error(msg)

    def debug(self, msg):
        msg = self._get_msg_info(msg)
        self.logger.debug(msg)

    def close(self):
        self.logger.removeHandler(self.fh)

    def _get_msg_info(self, msg):
        """
        用于打印日志
        :param info: dict
        :return: str
        """
        if isinstance(msg, dict):
            msg_info = ''
            for k, v in msg.items():
                msg_info = msg_info + '{}={} '.format(k, v)

            return msg_info

        return msg


loggers_dict = {}


# 写log的时候最好使用一个实例, 不然可能会引起重复写的问题.
def logger(name):
    if name not in loggers_dict.keys():
        loggers_dict[name] = BaseLog(name)
    return loggers_dict[name]
