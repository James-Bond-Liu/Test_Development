# -*- coding: utf-8 -*-
# @Time :2021/8/5 20:07
# @Author : liufei
# @File :自定义元类.PY

# 创建一个自定义的元类，并用此元类来创建一个类
class MyMetaClass(type):
    """自定义的元类"""

    def __new__(cls, name, bases, attr_dict, *args, **kwargs):
        print('调用自定义的元类')
        return super().__new__(cls, name, bases, attr_dict)


class Test(metaclass=MyMetaClass):
    """利用自定义的元类创建类"""
    name = 'panda'


print(type(Test))  # <class '__main__.MyMetaClass'>
print(Test.name)
class MyClass(Test):
    """父类指定了元类，子类可以继承父类所指定的元类"""
    """MyClass类继承了Test类，在创建MyClass类时依然利用自定义的元类MyMetaClass类来创建"""
    pass
print(type(MyClass))  # <class '__main__.MyMetaClass'>

