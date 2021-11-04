# -*- coding: utf-8 -*-
# @Time :2021/7/21 20:41
# @Author : liufei
# @File :通用装饰器.PY

import time


def decorator(func):
    def wrapper(*args, **kwargs):  # 内层函数参数为（不定长参数，关键字参数），被装饰函数无论是否有参数都可以通过装饰器装饰。
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)

    return wrapper


@decorator
def func():
    time.sleep(0.8)
    print()


func(1, 2)  # 函数实际调用wrapper（）# 输出：0.800644397735595
