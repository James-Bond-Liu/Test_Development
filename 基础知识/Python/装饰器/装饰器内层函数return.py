# -*- coding: utf-8 -*-
# @Time :2021/7/22 20:51
# @Author : liufei
# @File :装饰器内层函数return.PY

import time


def deco(func):
    def wrapper():
        startTime = time.time()
        n = func()  # 当被装饰函数有return值时，装饰器内层函数也必须return函数
        endTime = time.time()
        msecs = (endTime - startTime) * 1000
        print("time is %d ms" % msecs)
        return n

    return wrapper


@deco
def func():
    time.sleep(1)
    return 'liufei'


e = func()
print(e)
