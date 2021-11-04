# -*- coding: utf-8 -*-
# @Time :2021/8/14 11:33
# @Author : liufei
# @File :作业.PY

"""
1、用一个队列来存储商品
2、创建一个专门生产商品的程类，当商品数量少于50时，新始生产商品，每次生产200个商品，每生产完一轮暂停1秒
3、创建一个专门消费商品的线程类，当商品数量大于10时就开始淌费，，循环消费，每次消费3个。当商品实例少于10的时候，暂停2秒
4、创建一个线程生产商品，5个线程消费商品
"""
import threading
import queue
import time

q = queue.Queue()


class Producer(threading.Thread):
    def run(self):
        # 判断队列中的商品数量是否<50，小于50就开始生产商品
        count = 0
        while True:
            if q.qsize() < 50:
                for i in range(200):
                    count = count + 1
                    goods = '——生产第{}商品'.format(count)
                    q.put_nowait(goods)
                    print("生产：", goods)
                time.sleep(1)


class Customer(threading.Thread):
    def run(self):
        # 判断队列中的商品数量是否>10,大于10开始消费
        while True:
            if q.qsize() > 10:
                for j in range(3):
                    print("消费：{}".format(q.get_nowait()))
            elif q.qsize() < 10:
                time.sleep(2)



if __name__ == '__main__':
    p = Producer()
    p.start()

    for i in range(5):
        c = Customer()
        c.start()

