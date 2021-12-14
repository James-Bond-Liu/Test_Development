# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ess_api
# @File     :ctrller-manage_energystorage_insert
# @Date     :2021/11/9 8:53
# @Author   :LiuFei
# @Email    :fei.liu@hxgroup.com
# @Software :PyCharm
-------------------------------------------------
"""
import requests
url = 'http://172.30.14.239:8080/ctrller-manager/energystorage/insert'
token = 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJjdXN0b21lci0xMTFkc3N0bnk5a3ciLCJjb2RlIjoibmJwIiwidG9rZW5JZCI6MTM1NDE4Mzk3ODYzOTM2LCJleHAiOjE2MzkwMTA5MjQsImlhdCI6MTYzNjQxODkyNCwib3duZXJfdHlwZSI6ImN1c3RvbWVyIiwibG9jYWwiOiJlbiJ9.CEsX41m2gAP3lFccKvpAl1iTVPhN_WkVvEiuKGyozySmYCzt0UDE0N--PdYwRsnLfZ-9ofupv6AQESocBWcokg'
header = {'Content-Type': 'application/json', 'authorization': token}
data ={
'inverterSn': "2114-59000511D",
'powerStation': None,
'productType': 9
}
res = requests.post(url=url, json=data, headers = header)
# print(res.json()['msg_code'])

print(res.json())
print(res.status_code)