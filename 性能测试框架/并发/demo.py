# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ess_api
# @File     :demo
# @Date     :2021/11/17 10:01
# @Author   :LiuFei
# @Email    :fei.liu@hxgroup.com
# @Software :PyCharm
-------------------------------------------------
"""
import requests
import time, random
import threading



class ThreadRequests(threading.Thread):
    def run(self):
        for i in range(1000):
            data = {
                'adress': "power005",
                'agent': 136879273971712,
                'chargingType': None,
                'countryValue': "CN",
                'currencyUnit': 3,
                'customer': 136006800011265,
                'downPrice': [{'price': "1.2", 'startTime': 0, 'endTime': 86400}],
                'installer': None,
                'installerName': "",
                'isShown': 1,
                'latitude': "30",
                'longitude': "120",
                'name': random.randint(1, 999999999),
                'position': "",
                'pvCapacity': 1000,
                'systemType': 1,
                'timezone': 94,
                'timezoneName': "",
                'upPrice': [{'price': "1.2", 'startTime': 0, 'endTime': 86400}]
            }
            token = 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJjdXN0b21lci0wMDAwMDAwMDAwMDAwMDAiLCJjb2RlIjoibmJwIiwidG9rZW5JZCI6MTM2ODc5MDY0MjU2NTEyLCJleHAiOjE2Mzk3MDc0MjQsImlhdCI6MTYzNzExNTQyNCwib3duZXJfdHlwZSI6Im9wZXJhdG9yIiwibG9jYWwiOiJlbiJ9.UaLZ220a9T0f1Urh15bqO_Fov4xKmmXr7PyNz_00iEJbEDEVeXGZCuCpcU0J_C3LFcKujvnFsAw8woJSTprSnQ'
            header = {"Content-Type": "application/json", "authorization": token}
            res = requests.post(url='http://172.30.14.239:8080/ctrller-manager/powerstation/insert', json=data, headers = header)
            print(res.status_code)
            print(res.json())
            # print(f"线程{}")

def main():
    start_time=time.time()
    li = [ThreadRequests() for i in range(50)]
    for x in li:
        x.start()
    for n in li:
        n.join()
    end_time=time.time()
    print(f"50个线程进行创建电站，每个线程发送1000个请求耗时{end_time-start_time}")
main()