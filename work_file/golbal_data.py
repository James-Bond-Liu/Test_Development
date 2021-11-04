# -*- coding: utf-8 -*-
# @Time :2021/7/8 21:12
# @Author : liufei
# @File :golbal_data.PY

import requests


def http_request():
    data = {'name': 'xiaoming', 'pwd': 111, 'number': 1}
    res = requests.get(url='http://127.0.0.1:8888/login', params=data)
    print(res.json())
http_request()
