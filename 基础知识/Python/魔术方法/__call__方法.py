# -*- coding: utf-8 -*-
# @Time :2021/7/25 15:41
# @Author : liufei
# @File :__call__方法.PY

class Test(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def one(self):
        print('{0}岁的{1}正在爬'.format(self.age, self.name))

    def __call__(self, *args, **kwargs):  # 当把这个类对象当做函数调用时，自动触发这个方法
                                            # 如果没有这个方法，则会TypeError: 'Test' object is not callable
        s = '自动触发调用__str__方法'
        return s
t = Test('panda', 4)
t()  # 让这个类对象，像函数一样可以把调用
print(t())