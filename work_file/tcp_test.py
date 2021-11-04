# -*- coding: utf-8 -*-
# @Time :2021/7/8 11:17
# @Author : liufei
# @File :fsdfasd.PY

import threading
import socket
import time
from work_file.data import GetData

class High_Concur():
    def __init__(self, host, port, message):
        self.host = host
        self.port = port
        # self.message = message

    def send(self):
        test_data=GetData("*").test_data()
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        client.connect((self.host, self.port))
        # for x in range(10):
        for n in test_data:
            client.send(n.strip("\n").encode())
            time.sleep(180)
        client.close()


if __name__ == '__main__':
    hc = High_Concur()
    for i in range(0, 100001):
        thread = threading.Thread(target=hc.send())
        print(thread.is_alive())
    print(threading.enumerate())
