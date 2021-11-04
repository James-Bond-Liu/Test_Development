# -*- coding: utf-8 -*-
# @Time :2021/7/8 15:18
# @Author : liufei
# @File :fgfg.PY

import threading
import socket
import time
import flask
from flask import request

class High_Concur():

    def __init__(self, host, port, file_name):
        self.host = host
        self.port = port
        self.file_name = file_name

    server = flask.Flask(__name__)

    @server.route('/login', methods=['get', 'post'])
    def login(self):
        username = request.values.get('name')
        pwd = request.values.get('pwd')
        number_service = request.values.get('number')
        if username and pwd:
            if username == 'xiaoming' and pwd == '111':
                resu = {'code': 200, 'message': '登录成功', 'Number': number_service}
                # return json.dumps(resu, ensure_ascii=False)  # 将字典转换为json串, json是字符串
                return number_service

    def test_data(self):
        with open(self.file_name, mode='r') as f:
            row_data = f.readlines()
            return row_data

    def send(self):
        data = self.test_data()
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        client.connect((self.host, self.port))
        for n in data:
            if self.login == 1:
                client.send(n.strip("\n").encode())
                time.sleep(0.5)
            elif self.login == 0:
                client.close()


if __name__ == '__main__':
    hc = High_Concur('192.168.25.28', 999, r'liufei.txt')
    hc.server.run(debug=True, port=8888, host='0.0.0.0')
    for i in range(0, 50000):
        thread = threading.Thread(target=hc.send())
        print(thread.is_alive())
    hc.server.run(debug=True, port=8888, host='0.0.0.0')
    print(threading.enumerate())
