# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ESS_API
# @File     :read_config
# @Date     :2021/8/13 10:37
# @Author   :Liu Fei
# @Software :PyCharm
-------------------------------------------------
"""
import configparser
from 性能测试框架.conf.project_path import *

class ReadConfig():

    def readconfig(self, section, option):
        conf = configparser.ConfigParser()
        conf.read(filenames=conf_path, encoding='utf-8')
        return conf.get(section=section, option=option)


if __name__ == '__main__':
    a = ReadConfig().readconfig('MODE','data')
    print(a)
    print(type(eval(a)))