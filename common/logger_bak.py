#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/4 18:41
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : logger_bak.py
# @Software: PyCharm

import logging
from logging import handlers
from conf.setting import LOG_PATH


class Logger(object):

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls,*args)
        return cls.__instance

    def __init__(self,logger='root'):
        self.formatter = logging.Formatter('[%(asctime)s %(name)s %(levelname)s %(module)s %(pathname)s %(funcName)s Line:%(lineno)s]:%(message)s')
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        self.filelogger = handlers.RotatingFileHandler(filename=LOG_PATH,
                                                       mode='a',
                                                       maxBytes=10485760,#10M
                                                       backupCount=10,#最多备份10个
                                                       encoding='utf-8')
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.DEBUG)

        self.filelogger.setFormatter(self.formatter)
        self.console.setFormatter(self.formatter)
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)

    def debug(self,msg=None):
        self.logger.debug(msg)

    def info(self,msg=None):
        self.logger.info(msg)

    def warning(self,msg=None):
        self.logger.warning(msg)

    def error(self,msg=None):
        self.logger.error(msg)

    def exception(self,msg=None):
        return self.logger.exception(msg)

    def critical(self,msg=None):
        self.logger.critical(msg)



logger = Logger()


if __name__ == '__main__':
    # logger.logger.debug ('this is a debug')
    # logger.logger.info ('this is a info')
    # logger.logger.warning ('this is a warning')
    # logger.logger.warn ('this is a warn')
    # logger.logger.error ('this is a error')
    # logger.logger.exception ('this is a exception')
    # logger.logger.critical ('this is a critical')

    debug = 'this is a debug'
    info = 'this is a info'
    warning = 'this is a warning'
    error = 'this is a error'
    exception = 'this is a exception'
    critical = 'this is a critical'
    logger.debug(debug)
    logger.info(info)
    logger.warning(warning)
    logger.error(error)
    # logger.exception(exception)
    logger.critical(critical)