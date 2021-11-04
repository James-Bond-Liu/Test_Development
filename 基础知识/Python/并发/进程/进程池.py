# -*- coding: utf-8 -*-
# @Time :2021/8/15 14:23
# @Author : liufei
# @File :进程池.PY

from multiprocessing import Manager, Pool
import os, time, random



def work():
    print("执行任务，进程id{}".format(os.getpid()))
    time.time(0.5)  # 加入时间暂停，是为了让任务可以通过多个进程执行。
                    # 否则任务太简单，一个进程就足够执行完毕了


if __name__ == '__main__':

    # 创建进程池（最大三个进程）
    pool = Pool(3)

    for i in range(100):  # 给进程池创建100个任务，然后三个进程轮流执行这100个任务
        pool.apply_async(func=work)

    pool.close()  # 关闭进程池，使其不再接受新任务
    pool.join()  # 使主进程阻塞，等待子进程执行完毕后，再往下执行
    print("****")
