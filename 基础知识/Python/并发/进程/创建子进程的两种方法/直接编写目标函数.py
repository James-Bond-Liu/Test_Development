import os
import time
from multiprocessing import Process

def work(name):
    print(f'{name} running，进程ID为{os.getpid()}')
    time.sleep(1)
    print(f'{name} ending，进程ID为{os.getpid()}')

if __name__ == '__main__':  # 创建子进程的代码必须放在main函数下面
    name_list = ['panda', 'cat', 'dog', 'tiger']
    p_list = []
    for i in name_list:
        p = Process(target=work, args=(i,))  # 目标函数需要的参数以元组形式传入，单个参数也必须加“，”否则不是元组
        p_list.append(p)
        p.start()
    print('现在在主进程中')
    for j in p_list:
        j.join()  # 等待所有的子进程结束，代码再往下执行
    print('主进程结束')