# -*- coding: utf-8 -*-
# @Time :2021/8/8 15:30
# @Author : liufei
# @File :使用thread类创建线程.PY

import threading
import time


def fun1():
    for i in range(5):
        print("------执行fun1------")
        time.sleep(1)


def fun2():
    for j in range(6):
        print("------执行fun2------")
        time.sleep(1)


def main():
    start_time = time.time()
    # 创建一个线程对象t1，执行fun1
    t1 = threading.Thread(target=fun1, name='thread1')

    # 创建一个线程对象t2，执行fun2
    t2 = threading.Thread(target=fun2, name='thread2')

    # 开始执行thread1线程，此时真正开始创建了线程
    t1.start()  # start只是用来启动线程，线程的操作的方法是在thread类中的run中执行的

    # 返回线程是否正在活动，布尔值
    print(t1.is_alive())

    # 开始执行thread2线程
    t2.start()

    # 返回正在运行的线程
    print(threading.enumerate())

    # 设置主线程等待子线程thread1执行10秒，如果子线程在10秒内就执行完成，主线程自动向下执行。
    # 不传时间参数，默认等待该子线程执行完毕后，再继续执行主线程。
    t1.join(10)
    t2.join()

    end_time = time.time()
    print("耗时{}：".format(end_time - start_time))


if __name__ == '__main__':
    main()

"""
线程执行逻辑：
执行代码文件，会自动创建一个主线程，在主线程执行过程中，代码又创建了两个子线程thread1和thread2，这两个子线程去执行相关的操作，
同时主线程不会等待子线程执行（除非强迫主线程等待子线程执行完成join），会自动向下执行代码相关操作。这三个线程是同时一起工作的。
"""
