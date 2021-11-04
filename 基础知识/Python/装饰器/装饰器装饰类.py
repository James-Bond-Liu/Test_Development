# -*- coding: utf-8 -*-
# @Time :2021/7/21 20:41
# @Author : liufei
# @File :装饰器装饰类.PY

def f1(func):
    def fun(*args, **kwargs):
        print('这是一个装饰类的装饰器')
        return func(*args, **kwargs)  # 装饰器用来装饰类时，一定必须将被装饰的类返回出来。

    return fun


@f1
class Hero():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def move(self):
        print('{0}岁的{1}正在移动'.format(self.age, self.name))

    def demo(self):
        print('装饰器装饰类后，类下的所有方法都具有了扩展后的功能')


a = Hero('panda', 4)
a.move()
a.demo()
