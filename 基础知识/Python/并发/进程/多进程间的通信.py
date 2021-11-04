# -*- coding: utf-8 -*-
# @Time :2021/8/14 15:50
# @Author : liufei
# @File :进程间的通信.PY

import time
import requests
# from queue import Queue
from multiprocessing import Process, Queue


# 创建一个队列，添加十个任务
# q = Queue()
# for i in range (10):
#     q.put_nowait('http://www.baidu.com')


def work1(q):
    while True:
        if not q.empty():  # 判断队列中是否有任务
            data = q.get(timeout=3)  # 从队列获取任务
            requests.get(data)  # 执行任务
            print("work1正在执行任务")
        else:
            break


def work2(q):
    while True:
        if not q.empty():  # 判断队列中是否有任务
            data = q.get(timeout=3)  # 从队列获取任务
            requests.get(data)  # 执行任务
            print("work2正在执行任务")
            print()
        else:
            break

if __name__ == '__main__':  # 进程一定要在__name__ == '__main__'下执行
                            # 避免无限创建子进程
    q = Queue()
    for i in range(10):
        q.put_nowait('http://www.baidu.com')
    # 创建两个进程
    # 将队列当作一个参数传入进程目标函数中，这样两个进程就能共享同一个队列（全局变量）
    p1 = Process(target=work1, args=(q,))
    p2 = Process(target=work2, args=(q,))
    # 启动两个进程
    p1.start()
    p2.start()
    # 获取两个进程的进程id
    print(p1.pid)
    print(p2.pid)
    p1.join()
    p2.join()
    print("****")
    # p1.terminate()
    # p2.terminate()
