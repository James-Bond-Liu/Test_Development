from multiprocessing import Process
import requests
import time

def run():
    res = requests.request(method='GET', url='https://www.baidu.com/')
    print(res.elapsed.total_seconds())


if __name__ == '__main__':
    start_time = 20
    while True:
        for i in range(1000):
            p = Process(target=run)
            p.start()
            end_time = 30
            time = end_time-start_time
            if time == 30:  # 持续发起请求30分钟
                break






