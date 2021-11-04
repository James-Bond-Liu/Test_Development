# -*- coding: utf-8 -*-
# @Time :2021/8/16 20:02
# @Author : liufei
# @File :进程池执行.PY

from multiprocessing import Queue, Manager, Pool
from multiprocessing import Process
import requests
import time

def work(q):
    # while q.qsize()>0:
        url = q.get()
        requests.get(url = url)

if __name__ == '__main__':
    start_time = time.time()
    q = Manager().Queue()
    for i in range(1000):
        q.put_nowait('http://www.baidu.com')
    pool = Pool(3)
    # for j in range(3):
    for j in range(q.qsize()):
        pool.apply_async(work, args=(q,))
    pool.close()
    pool.join()
    end_time = time.time()
    print(end_time-start_time)  # 6.226366281509399