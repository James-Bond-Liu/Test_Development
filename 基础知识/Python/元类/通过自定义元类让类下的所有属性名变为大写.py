# -*- coding: utf-8 -*-
# @Time :2021/8/5 20:23
# @Author : liufei
# @File :通过自定义元类让类下的所有属性名变为大写.PY

class MyMetaClass(type):
    """自定义的元类"""

    def __new__(cls, name, bases, attr_dict, *args, **kwargs):
        print('调用自定义的元类')
        for key, value in attr_dict.items():
            attr_dict.pop(key)
            attr_dict[key.upper()] = value
        return super().__new__(name, bases, attr_dict)


class Test(metaclass=MyMetaClass):
    """利用自定义的元类创建类"""
    name = 'panda'

# print(Test.__dict__)


