# -*- coding: utf-8 -*-
# @Time :2021/8/15 15:10
# @Author : liufei
# @File :进程池内多进程通信.PY

from multiprocessing import Manager, Pool
import os
import requests

# def work(q):
#     while True:
#         if not q.empty():  # 判断队列中是否有任务
#             data = q.get(timeout=3)  # 从队列获取任务
#             requests.get(data)  # 执行任务
#             print("正在执行任务,进程id{}".format(os.getpid()))
#         else:
#             break


def work(q,a):
    data = q.get_nowait()  # 从队列获取任务
    requests.get(data)  # 执行任务
    print("正在执行任务,进程id{}".format(os.getpid()))
    print(a)

if __name__ == '__main__':
    q = Manager().Queue()  # 创建进程池内的队列，用来存储任务
    for i in range(100):  # 创建100个任务
        q.put_nowait('http://www.baidu.com')

    pool = Pool(5)  # 创建一个进程池，最多创建5个进程

    # for j in range(5):
    #     pool.apply_async(work, args=(q,))

    while True:
        if q.qsize() > 0:  # 只要队列中有任务，就从从进程池中开启一个进程去执行任务
            pool.apply_async(work, args=(q,))  # 给进程池添加队列中同等数量的任务
        else:
            break
    pool.close()
    pool.join()

