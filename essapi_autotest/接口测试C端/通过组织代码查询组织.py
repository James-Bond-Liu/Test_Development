# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ess_api
# @File     :通过组织代码查询组织
# @Date     :2021/10/15 9:21
# @Author   :LiuFei
# @Email    :fei.liu@hxgroup.com
# @Software :PyCharm
-------------------------------------------------
"""
import requests

data = {
'code': "CN7035",
'include_children': 'true',
'limit': 50,
'parent_id': 0,
'start': 0
}

url = "http://172.30.14.239:8080/ctrller-manager/powerstation/update"
token = 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJjdXN0b21lci0wMDAwMDAwMDAwMDAwMDAiLCJjb2RlIjoibmJwIiwidG9rZW5JZCI6MTM0NTY4MDE5NTA1MTUyLCJleHAiOjE2Mzg2MDU0MzIsImlhdCI6MTYzNjAxMzQzMiwib3duZXJfdHlwZSI6Im9wZXJhdG9yIiwibG9jYWwiOiJlbiJ9.WT75CITmF8eq6nlHQk7fiNy61-J2cCYE7S41EMkIRc1pVo9bXj_RVnjCUPPti0DaEiOGakwuNV6TO5K9_rQCog'
header = {"Content-Type": "application/json", "authorization": token}
data ={
'adress': "power005",
'agent': 134569070178304,
'batteryCapacity': "0",
'batteryCapacityUnit': "kWp",
'batterySOC': "0",
'capacity': "0",
'capacityUnit': "kWp",
'chargingType': None,
'chargingTypeName': None,
'country': 45,
'countryName': "中国",
'countryValue': "CN",
'currencySymbol': "¥",
'currencyUnit': 3,
'customer': 134568074031105,
'downPrice': [{'endTime': 86400, 'id': 517, 'powerStation': 406, 'price': 1.2, 'startTime': 0}],
'eTotalToGrid': "0",
'eTotalToGridUnit': "kWh",
'eoutDaily': "0",
'eoutDailyUnit': "kWh",
'eoutMonth': "0",
'eoutMonthUnit': "kWh",
'gridActivePower': "0",
'gridActivePowerUnit': "kW",
'id': 193,
'isShown': 1,
'latitude': "30",
'longitude': "120",
'monthProfit': "0",
'name': "powerAutotest005",
'position': "120,30",
'productSeries': None,
'productSeriesName': None,
'pvCapacity': "1000",
'pvCapacityUnit': "kWp",
'registrationTime': 1634798011000,
'status': 2,
'systemType': 1,
'systemTypeName': "光伏并网系统",
'timezone': 94,
'timezoneName': "(UTC+08:00)北京",
'todayProfit': "0",
'totalProfit': "0",
'upPrice': [{'endTime': 86400, 'id': 514, 'powerStation': 406, 'price': 1.2, 'startTime': 0}],
'updateTime': 0,
'value': "Asia/Shanghai",
}

res = requests.post(url=url, json=data, headers = header)
print(res.status_code)
print(res.json())
