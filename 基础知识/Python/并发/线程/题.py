# -*- coding: utf-8 -*-
# @Time :2021/8/8 18:42
# @Author : liufei
# @File :多线程全局变量.PY

import time
import threading
import queue
# 多线程共享全局变量的问题

"""
多个线程之间是互相影响全局变量的
但是也有问题，当线程执行次数比较多时就有影响了
"""
q = queue.Queue()
a = 0
def fun1():
    global a
    for i in range(10000000):
        a = a + 1
        q.put_nowait(a)


def fun2():
    for j in range(10000000):
        a = q.get_nowait()
        a = a + 1
        q.put_nowait(a)

start_time = time.time()
t1 = threading.Thread(target=fun1)
t2 = threading.Thread(target=fun2)
t1.start()
t2.start()
t1.join()
t2.join()
end_time = time.time()
print('总耗时{}'.format(end_time-start_time))
print(a)  # 理论输出20000000，实际输出12327391

"""
总耗时1.5888240337371826
12530560
"""