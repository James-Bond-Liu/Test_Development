from multiprocessing import Process
import requests
import os
import datetime


class My_Process(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        while True:
            start_time = datetime.datetime.now()
            print(self.name)
            print(os.getpid())
            end_time = datetime.datetime.now()
            final_time = (end_time - start_time).seconds
            if final_time >= 1800:
                break



if __name__ == '__main__':
    for i in range(1000):
        my_process = My_Process("my_process进程"+str(i))
        my_process.start()