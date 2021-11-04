# -*- coding: utf-8 -*-
# @Time :2021/8/16 19:31
# @Author : liufei
# @File :进程执行.PY

# 进程，任务数3个小于cpu数（8）个，可以并行。三个任务可以同时执行

from multiprocessing import Queue, Manager
from multiprocessing import Process
import requests
import time

q = Queue()  # 进程队列，可以在多个进程间通信

def work(q):
    while q.qsize()>0:
        url = q.get()
        requests.get(url=url)



if __name__ == '__main__':
    for i in range(1000):
        q.put('http://www.baidu.com')
    start_time = time.time()
    p1 = Process(target=work, args=(q,))
    p2 = Process(target=work, args=(q,))
    p3 = Process(target=work, args=(q,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    end_time = time.time()
    print(end_time-start_time)  # 5.929177761077881