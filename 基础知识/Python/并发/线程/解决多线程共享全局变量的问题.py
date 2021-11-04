# -*- coding: utf-8 -*-
# @Time :2021/8/8 18:42
# @Author : liufei
# @File :多线程全局变量.PY

import time
import threading

# 解决多线程共享全局变量的问题

# 创建一个锁
meta = threading.Lock()
a = 0
def fun1():
    global a
    for i in range(10000000):
        # 上锁
        meta.acquire()
        a = a+1
        # 释放锁
        meta.release()

def fun2():
    global a
    for j in range(10000000):
        meta.acquire()
        a = a + 1
        meta.release()

start_time = time.time()
t1 = threading.Thread(target=fun1)
t2 = threading.Thread(target=fun2)
t1.start()
t2.start()
t1.join()
t2.join()
end_time = time.time()
print('总耗时{}'.format(end_time-start_time))
print(a)
"""
上锁前：
总耗时1.5888240337371826
12530560

上锁后：
总耗时12.35008955001831
20000000
"""

