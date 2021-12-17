import os
import time
from multiprocessing import Process

class Work(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

# 通过重写父类Process的run方法
    def run(self):
        print(f'{self.name} running，进程ID为{os.getpid()}')
        time.sleep(1)
        print(f'{self.name} ending，进程ID为{os.getpid()}')

if __name__ == '__main__':
    name_list = ['panda', 'cat', 'dog', 'tiger']
    p_list = []
    for i in name_list:
        p = Work(i)  # 直接创建Work的实例对象即创建进程
        p_list.append(p)
        p.start()  # 进程启动时，会自动调用重写的run方法
    print('现在在主进程中')
    for j in p_list:
        j.join()
    print('主进程结束')




