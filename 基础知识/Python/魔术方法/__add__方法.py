# -*- coding: utf-8 -*-
# @Time :2021/7/27 20:31
# @Author : liufei
# @File :__add__方法.PY

class Demo():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):  # self代表+号前面的对象，other代表+号后面的对象
        print('对象之间使用了+号')
        return self.age + other.age


a = Demo('panda', [2, 3, 4])
b = Demo('dog', [5, 6, 7])
print(a + b)  # +号，自动触发类中重写的__add__(self,other)方法
