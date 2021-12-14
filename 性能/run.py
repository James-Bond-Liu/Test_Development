from multiprocessing import Process
import requests
import time

# def run():
#     res = requests.request(method='GET', url='https://www.baidu.com/')
#     print(res.elapsed.total_seconds())

class My_Process(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        while True:
            print(self.name)



if __name__ == '__main__':
    for i in range(1000):
        my_process = My_Process("my_process进程"+str(i))
        my_process.start()
    # while True:
    #     for i in range(1000):
    #         p = Process(target=run)
    #         p.start()
    #         end_time = 30
    #         time = end_time-start_time
    #         if time == 30:  # 持续发起请求30分钟
    #             break






