# -*- coding: utf-8 -*-
# @Time :2021/7/25 14:57
# @Author : liufei
# @File :__new__方法.PY

class Test(object):
    number = 123
    def __new__(cls, *args, **kwargs):  # 重写父类object类中__new__方法
        obj = object.__new__(cls)  # 调用父类中的方法，创建类实例
        print('重写__new__方法')
        return obj

t = Test()  # 在类实例化对象时首先触发__new__方法
print(t)
print(t.number)