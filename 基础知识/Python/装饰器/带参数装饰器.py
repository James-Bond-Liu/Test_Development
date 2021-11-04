# -*- coding: utf-8 -*-
# @Time :2021/7/21 20:41
# @Author : liufei
# @File :带参数装饰器.PY

import time


# 带有参数的装饰器
def deco(func):
    def wrapper(a, b):
        startTime = time.time()
        func(a, b)
        endTime = time.time()
        msecs = (endTime - startTime) * 1000
        print("time is %d ms" % msecs)

    return wrapper


@deco
def func(a, b):
    print("hello，here is a func for add :")
    time.sleep(1)
    print("result is %d" % (a + b))


if __name__ == '__main__':
    func(3, 4)  # 经过语法糖装饰之后，执行func(3，4)，实际执行的是wrapper(3,4)