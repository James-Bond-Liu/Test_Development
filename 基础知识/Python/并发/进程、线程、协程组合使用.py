# -*- coding: utf-8 -*-
# @Time :2021/8/19 20:21
# @Author : liufei
# @File :进程、线程、协程组合使用.PY

"""
10000个请求，用2个进程，每个进程3个线程，每个线程5个协程来完成请求
"""

import time
import requests
from threading import Thread
from multiprocessing import Process, Queue
import gevent

# 需求：10000个请求，用2个进程，3个线程，5个协程来完成

def gevent_work(q, gname):
    """
    每个协程的工作函数
    :param q:
    :param gname:
    :return:
    """
    count = 0
    while not q.empty():
        url = q.get(timeout=0.01)
        requests.get(url)
        gevent.sleep(0.001)
        count = count+1
    print('----------------协程{}执行了{}个任务----------------'.format(gname, count))


def thread_work(q, tname):
    """
    每个线程的工作函数，在线程中开启5个协程
    :param q:
    :param tname:
    :return:
    """
    g_list = []
    for i in range(5):
        gname = '{}-g-{}'.format(tname, i)
        print('创建协程{}'.format(gname))
        g = gevent.spawn(gevent_work, q, gname)
        g_list.append(g)
    gevent.joinall(g_list)



def process_work(q, pname):
    """
    每个进程执行的任务函数，在每个进程中开启三个线程
    :param q: 进程间通信的队列
    :param pname: 进程名字
    :return:
    """
    # 创建三个线程
    thread_list = []
    for i in range(3):
        tname = '{}-th-{}'.format(pname,i)
        print('创建线程{}'.format(tname))
        t = Thread(target=thread_work, args=(q, tname))
        thread_list.append(t)
        t.start()
    for t in thread_list:
        t.join()

# 装饰器
def deco(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
    return wrapper


#创建一个main函数来控制程序的执行
@deco
def main():
    # 创建10000个请求的队列
    q = Queue()
    for i in range(10000):
        q.put('http://www.baidu.com')
    print('队列创建完成，数量{}'.format(q.qsize()))
    pro_list = []
    for i in range(2):
        pname = 'pro-{}'.format(i)
        print('创建进程{}'.format(pname))
        p = Process(target=process_work, args=(q,pname))
        p.start()
        pro_list.append(p)

    # 让主进程等待子进程执行完毕后再往下执行
    for p in pro_list:
        p.join()

if __name__ == '__main__':
    main()