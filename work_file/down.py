# -*- coding: utf-8 -*-
# @Time :2021/7/8 19:29
# @Author : liufei
# @File :down.PY
import threading
import socket
import time
from work_file import golbal_data


class High_Concur():

    def __init__(self, host, port, file_name):
        self.host = host
        self.port = port
        self.file_name = file_name

    def test_data(self):
        with open(self.file_name, mode='r') as f:
            row_data = f.readlines()
            return row_data

    def send(self):
        number = getattr(golbal_data, 'number')
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        client.connect((self.host, self.port))
        data = self.test_data()
        while True:
            for n in data:
                if number == 1:
                    client.send(n.strip("\n").encode())
                else:
                    time.sleep(1)


if __name__ == '__main__':
    hc = High_Concur('192.168.25.28', 999, r'liufei.txt')
    thread_list=[]
    for i in range(0, 50000):
        x=threading.Thread(target=hc.send())
        thread_list.append(x)
    for a in thread_list:
        if number ==1:
            a.start()
        else:
            time.sleep(1)



    #     if number == 1:
    #     #         thread.hc.send()
    #     #     else:
    #     #         time.sleep(1)
    #     #     print(thread.is_alive())
    #     # print(threading.enumerate())
