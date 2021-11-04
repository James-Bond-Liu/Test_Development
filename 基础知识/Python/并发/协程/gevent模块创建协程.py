# -*- coding: utf-8 -*-
# @Time :2021/8/17 19:51
# @Author : liufei
# @File :gevent模块创建协程.PY

# 协程：gevent协程存在于线程之中，线程默认不会等待协程执行，
# spawn：开启协程（第一个参数为协程要执行的任务）
# join；让线程等待协程执行协程之间切换的条件

#协程切换的条件耗时等待的情况下才会切换。如果没下面的1或2条件，协程不会切换，相当于一个主线程没有协程依次执行完成
# 1、gevent.sleep(time) 强制协程休眠一定时间然后切换协程
# 2、gevent的补丁：gevent.monkey.patch_all()，当协程有耗时操作时主动切换协程

"""
import gevent

def work1():
    for i in range(10):
        print("——work1——{}".format(i))
        gevent.sleep(0.1)  # 强制等待一定时间，让协程切换执行任务


def work2():
    for i in range(10):
        print("——work2——{}".format(i))
        gevent.sleep(0.1)

# 创建两个协程
# spawn：开启协程（第一个参数为协程要执行的任务，可以传入目标函数所需的参数）
g1 = gevent.spawn(work1)  # 用gevent创建的协程，创建完成就会立即执行任务
g2 = gevent.spawn(work2)  # 不像线程、进程需要start方法才开始执行任务


# 迫使线程等待两个协程执行完成后再往下进行
# 线程默认是不等待协程执行完成的
g1.join()
g2.join()"""

from gevent import monkey
import queue
import requests
import gevent
import time

gevent.monkey.patch_all()  # 当协程有耗时操作时主动切换协程，不局限于gevent.sleep()
# 这个等待补丁建议在单线程里使用。
q = queue.Queue()
for i in range(1000):
    q.put('http://www.baidu.com')
def work():
    while q.qsize()>0:
        url = q.get()
        requests.get(url)


stime=time.time()
# 创建两个协程
# spawn：开启协程（第一个参数为协程要执行的任务，可以传入目标函数所需的参数）
g1 = gevent.spawn(work)  # 用gevent创建的协程，创建完成就会立即执行任务
g2 = gevent.spawn(work)  # 不像线程、进程需要start方法才开始执行任务
"""协程几乎不耗费资源可以开启大量协程，做并发非常合适"""

# 迫使线程等待两个协程执行完成后再往下进行
# 线程默认是不等待协程执行完成的
g1.join()
g2.join()
# work()  # 单线程执行1000个任务耗时21秒，两个协程执行1000任务耗时9秒
etime = time.time()

print(etime-stime)