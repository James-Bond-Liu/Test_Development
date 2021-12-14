# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ESS_API
# @File     :out_log
# @Date     :2021/8/13 10:42
# @Author   :Liu Fei
# @Software :PyCharm
-------------------------------------------------
"""
import logging
from conf.project_path import *

class OutLog(object):

    """自定义一个日志输出器"""
    def out_log(self):
        logger = logging.getLogger('HESS')
        logger.setLevel('DEBUG')
        if not logger.handlers:
            handler_file = logging.FileHandler(filename=log_path, encoding='utf-8')
            handler_stream = logging.StreamHandler()
            formatter = logging.Formatter(fmt="%(name)s %(asctime)s %(levelname)s %(filename)s %(message)s",
                                        datefmt="%Y-%m-%d %H:%M:%S")
            handler_stream.setFormatter(formatter)
            handler_file.setFormatter(formatter)
            logger.addHandler(handler_stream)
            logger.addHandler(handler_file)
        return logger


if __name__ == '__main__':
    logger = OutLog().out_log()
    logger.info("jdkfj")
