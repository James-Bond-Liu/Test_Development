# -*- coding: utf-8 -*-
# @Time :2021/8/14 12:30
# @Author : liufei
# @File :多进程.PY

import time
from multiprocessing import Process

# 多进程执行多任务

def work1():
    for i in range(100):
        print("任务1")
        time.sleep(1)

def work2():
    for i in range(100):
        print("任务2")
        time.sleep(2)


if __name__ == '__main__':  # 进程一定要在__name__ == '__main__'下执行

    # 创建两个进程
    p1 = Process(target=work1)
    p2 = Process(target=work2)
    # 启动两个进程
    p1.start()
    p2.start()
