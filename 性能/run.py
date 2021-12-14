import time
import requests
from threading import Thread
from multiprocessing import Process, Queue
import gevent

def gevent_work(q):
    while not q.empty():
        url = q.get(timeout=0.01)
        requests.get(url)
        gevent.sleep(0.01)


def thread_work(q, tname):
    gev_list = []
    for i in range(5):
        gname = f'{tname}-gev-{i}'
        print(f'创建协程{gname}')
        g = gevent.spawn(gevent_work, q, gname)
        gev_list.append(g)
    gevent.joinall(gev_list)



def process_work(q, pname):
    thread_list = []
    for i in range(3):
        tname = f'{pname}-th-{i}'
        print(f'创建线程{tname}')
        t = Thread(target=thread_work, args=(q, tname))
        t.start()
        thread_list.append(t)
    for t in thread_list:
        t.join()

def main():
    q = Queue()
    for j in range(1000):
        q.put('http://www.baidu.com')
    pro_list = []
    for i in range(2):
        pname = f'pro-{i}'
        print(f'创建进程{pname}')
        p = Process(target=process_work, args=(q, pname))
        p.start()
        pro_list.append(p)
    for p in pro_list:
        p.join()

main()
# class Run(Process):
#     def __init__(self, data):
#         super().__init__()
#         self.data = data
#
#     def run(self):
#         res = requests.request(method='**', url='**', json='**')
#         res.elapsed.total_seconds()
#
# if __name__ == '__main__':
#     for i in range(1000):
#         p = Run(data="****").run()
#         p.start()
#
#
#
#
