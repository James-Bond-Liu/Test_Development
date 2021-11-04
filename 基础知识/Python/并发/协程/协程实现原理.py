# -*- coding: utf-8 -*-
# @Time :2021/8/17 20:22
# @Author : liufei
# @File :协程实现原理.PY

"""
协程底层是通过生成器来实现的
"""

def work1():
    for i in range(10):
        print("——work1——{}".format(i))
        yield

def work2():
    for i in range(10):
        print("——work2——{}".format(i))
        yield


# 通过生成器实现多任务
g1 = work1()
g2 = work2()

while True:
    try:
        next(g1)
        next(g2)
    except:
        break
