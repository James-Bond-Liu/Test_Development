# -*- coding: utf-8 -*-
# @Time :2021/7/22 19:12
# @Author : liufei
# @File :用类实现装饰器（类装饰器）.PY

class Decorator():
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print('这是装饰器内层函数的功能')
        k = self.func()
        print('这里依然是装饰器内层函数的功能')
        return k

@Decorator
def test():
    print('这里是原函数的功能')

test()


@Decorator
class Demo():
    c = 10
    def one(self):
        print('*******')

d = Demo()
print(d.c)