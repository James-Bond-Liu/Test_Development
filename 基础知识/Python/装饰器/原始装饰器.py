# -*- coding: utf-8 -*-
# @Time :2021/7/13 12:42
# @Author : liufei
# @File :装饰器.PY

# 开放封闭原则：软件实体的的功能是可以扩展的，但是函数实体不能修改。
"""python装饰器就是用于拓展原来函数功能的一种函数，这个函数的特殊之处在于它的返回值也是一个函数，
使用python装饰器的好处就是在不用更改原函数的代码前提下给函数增加新的功能。"""

# 原始的装饰器
import time
"""
这里的deco函数就是最原始的装饰器，它的参数是一个函数，然后返回值也是一个函数。
其中作为参数的这个函数func()就在返回函数wrapper()的内部执行。
"""
def deco(func):
    def wrapper():
        startTime = time.time()
        s = func()
        endTime = time.time()
        msecs = (endTime - startTime)*1000
        print("time is %d ms" %msecs)
        return s
    return wrapper


@deco  # 相当于func = deco(func)
# 相当于将被装饰函数func的函数体作为参数传入装饰器函数deco中。执行deco函数，直接返回内层函数wrapper的函数体给func,
# 此时调用func()相当于执行内层函数wrapper()。
# @deco的作用等同于1、func = deco(func)；2、func()
def func():
    print("hello")
    time.sleep(1)
    print("world")

if __name__ == '__main__':
    # 调用func()函数，其实就是调用wrapper内层函数
    f = func #这里f被赋值为func，执行f()就是执行func()
    f()


