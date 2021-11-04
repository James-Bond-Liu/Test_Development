# -*- coding: utf-8 -*-
# @Time :2021/8/3 19:34
# @Author : liufei
# @File :ORM模型介绍.PY

"""
ORM解决的主要问题是对象和关系的映射,它通常将一个类和一张表一一对应,类的每个对象对应表中的一条记录,类的每个属性对应表中的每个字段。
ORM提供了对数据库的映射,不用直接编写SQL代码,只需操作对象就能对数据库的数据进行操作.让开发人员专注于业务逻辑的处理,提高了开发效率。
"""

# 用描述器简单实现一个ORM模型
class Model(object):
    def __init__(self):
        self.max_length = 5  # 限定字段最长为多少

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, str):  # 限定字段类型
            if len(value) < self.max_length:
                self.value = value
            else:
                raise ValueError('字符串长度最大为{}'.format(self.max_length))
        else:
            raise TypeError('只能输入字符串类型数据')

    def __delete__(self, instance):
        # del self.value
        self.value = None


class Test(object):
    attr = Model()


t = Test()
t.attr = 432
