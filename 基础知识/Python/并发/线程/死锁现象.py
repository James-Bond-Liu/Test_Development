# -*- coding: utf-8 -*-
# @Time :2021/8/9 20:08
# @Author : liufei
# @File :死锁现象.PY

import time
import threading

# 解决多线程共享全局变量的问题

# 创建两个锁
metaA = threading.Lock()
metaB = threading.Lock()
a = 0
def fun1():
    global a
    for i in range(10000000):
        # A上锁
        metaA.acquire()
        # B上锁
        metaB.acquire()
        print("-------1--------")
        a = a+1
        # 释放锁B
        metaB.release()
        # 释放锁A
        metaA.release()

def fun2():
    global a
    for j in range(10000000):
        # B上锁
        metaB.acquire()
        # A上锁
        metaA.acquire()
        print("-------2--------")
        a = a + 1
        # 释放锁A
        metaA.release()
        # 释放锁B
        metaB.release()

"""
fun1上完A锁后，打算上B锁，但是发现fun2已经上完B锁了，所以fun1只能等待fun2的B锁释放后才能继续
fun2上完B锁后，打算上A锁，但是发现fun1已经上完A锁了，所以fun2只能等待fun1的A锁释放后才能继续
所以这两个线程就在互相等待着对方释放锁，从而造成死锁现象。
"""


start_time = time.time()
t1 = threading.Thread(target=fun1)
t2 = threading.Thread(target=fun2)
t1.start()
t2.start()
# t1.join()
# t2.join()
end_time = time.time()
print('总耗时{}'.format(end_time-start_time))
print(a)


