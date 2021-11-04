# -*- coding: utf-8 -*-
# @Time :2021/8/9 18:17
# @Author : liufei
# @File :作业.PY

# 创建一个线程类，每个线程对地址url=http://httpbin.org/post发送100个请求，开启10个钱程对象，
# 同时发送，计算总的耗时，分析平局每个请求所需要的时间

import requests
import time
import threading

class ThreadRequests(threading.Thread):

    def run(self):
        for i in range(100):
            res = requests.post(url = 'http://httpbin.org/post')
            print("线程{}第{}次请求".format(self.name, i))

def main():
    start_time = time.time()
    # li = []
    # for j in range(10):
    #     li.append(ThreadRequests())
    # 利用列表推导式生成一个线程对象列表
    li = [ThreadRequests() for j in range(10)]
    # 对线程对象列表遍历启动线程
    for x in li:
        x.start()
    # 对线程列表对象遍历，让主线程等待每个线程执行完成之后，再往下执行
    for n in li:
        n.join()
    end_time = time.time()
    print('10个线程对象，每个线程发送100个请求总耗时{}'.format(end_time-start_time))

main()
