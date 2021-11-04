# -*- coding: utf-8 -*-
# @Time :2021/8/17 19:51
# @Author : liufei
# @File :greenlet模块创建协程.PY

from greenlet import greenlet
import time


def work1():
    for i in range(10):
        print("——work1——{}".format(i))
        g2.switch()  # 协程和生成器一样，会记录上次执行的位置。
                     # 执行g2.switch()会启动g2协程，同时work2函数里也有g1.switch()，
                     # 当执行到work2函数里的g1.switch()又会切换到work1函数。
                     # 等于实现了生成器里的next方法

def work2():
    for i in range(10):
        print("——work2——{}".format(i))
        g1.switch()

# 创建两个协程
g1 = greenlet(work1)
g2 = greenlet(work2)

# 执行协程
g1.switch()
# g2.switch()