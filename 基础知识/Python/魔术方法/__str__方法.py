# -*- coding: utf-8 -*-
# @Time :2021/7/25 15:08
# @Author : liufei
# @File :__str__方法.PY

class Test(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def one(self):
        print('{0}岁的{1}正在爬'.format(self.age, self.name))

    def __str__(self):
        s = '自动触发调用__str__方法'
        return s

t = Test('panda', 4)
t.one()
print(t)  # 在print时会自动调用类中的__str__方法