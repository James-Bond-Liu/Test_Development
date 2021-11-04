# -*- coding: utf-8 -*-
# @Time :2021/8/8 16:17
# @Author : liufei
# @File :继承Thread类创建线程.PY

import threading
import requests
# 通过继承Thread类创建线程

class RequestThread(threading.Thread):

    # 重写Thread类下的init方法必须继承父类的方法
    def __init__(self, url):
        self.url = url
        # super().__init__()
        threading.Thread.__init__(self)

    # Thread类中的start方法是用来创建并启动线程，run方法是真正执行线程操作的方法。
    # 此处重写run方法，将线程的操作直接写在run里。
    def run(self):
        for j in range(2):  # 每个线程发起两个请求
            res = requests.get(url=self.url)
            print('---线程{}---返回的状态码是{}'.format(threading.current_thread(),res.status_code))


if __name__ == '__main__':
    # 创建5个子线程，发起请求
    for i in range(5):
        t = RequestThread("http://www.baidu.com")  # 创建线程对象
        t.start()  # 创建线程并启动线程
