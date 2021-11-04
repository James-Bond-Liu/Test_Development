# -*- coding: utf-8 -*-
# @Time :2021/8/16 19:27
# @Author : liufei
# @File :线程执行.PY

# 线程，由于有GIL锁的存在，只能并发（三个任务不可能同时执行）

import queue
import threading
import time
from multiprocessing import Queue, Manager
import requests

q = queue.Queue()  # 线程队列只能在一个进程里面使用



# q3 = Manager().Queue()  # 进程池队列，可以在进程池中多个进程通信

for i in range(1000):
    q.put('http://www.baidu.com')

def work():
    while q.qsize()>0:
        url = q.get()
        requests.get(url=url)

def main():
    start_time = time.time()
    t1 = threading.Thread(target=work)
    t2 = threading.Thread(target=work)
    t3 = threading.Thread(target=work)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    end_time = time.time()
    print(end_time-start_time)  #5.427966117858887

if __name__ == '__main__':
    main()




