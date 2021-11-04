# -*- coding: utf-8 -*-
# @Time :2021/8/11 19:03
# @Author : liufei
# @File :CPU密集型.PY

import time
import threading
import requests
a = 0

def fun1():

    for i in range(1000):
        res = requests.get('http://www.baidu.com')

def fun2():

    for j in range(1000):
        res = requests.get('http://www.baidu.com')

# s_time = time.time()
# t1 = threading.Thread(target=fun1)
# t2 = threading.Thread(target=fun2)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# e_time = time.time()
# print(e_time-s_time)#1.4568605422973633

s_time = time.time()
fun1()
fun2()
e_time = time.time()
print(e_time-s_time)#1.4552624225616455
