# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ess_api
# @File     :ctrller-manager-powerstation-update
# @Date     :2021/11/5 9:47
# @Author   :LiuFei
# @Email    :fei.liu@hxgroup.com
# @Software :PyCharm
-------------------------------------------------
"""
import requests
url = 'http://172.30.14.239:8080/ctrller-manager/powerstation/update'
token = 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJjdXN0b21lci0xMHNqdTBid3lmcGMiLCJjb2RlIjoibmJwIiwidG9rZW5JZCI6MTM0Njk1Mjg1MTc0MjcyLCJleHAiOjE2Mzg2NjYxMTcsImlhdCI6MTYzNjA3NDExNywib3duZXJfdHlwZSI6ImN1c3RvbWVyIiwibG9jYWwiOiJlbiJ9.-C5Jti2zmZjmW1Xzrf-m0WgevAYhnMsz-erMFVopcjua4mXVErqdL8LL3fiwW5sQObGjwLSOlJlxPYlHuDGqyA'
"""
agent字段输入不存在的id,期望失败，实际失败，pass
        输入None，期望失败，实际失败，pass
        输入字符，期望失败，实际失败，pass
        输入特殊字符，期望失败，实际失败，pass
"""
data1 = {
'adress': "power201",
'agent': '***&&5%',
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
'customer': 134521334804481,
'downPrice': [{'endTime': 86400, 'id': 194, 'powerStation': 205, 'price': 1.2, 'startTime': 0}],
'eTotalToGrid': "0",
'eTotalToGridUnit': "kWh",
'eoutDaily': "0",
'eoutDailyUnit': "kWh",
'eoutMonth': "0",
'eoutMonthUnit': "kWh",
'gridActivePower': "0",
'gridActivePowerUnit': "kW",
'id': 202,
'isShown': 1,
'latitude': "30",
'longitude': "120",
'monthProfit': "0",
'name': "powerAutotest002",
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
'upPrice': [{'endTime': 86400, 'id': 196, 'powerStation': 205, 'price': 1.2, 'startTime': 0}],
'updateTime': 0,
'value': "Asia/Shanghai",
}
"""
电站名称name字段输入特殊字符_-,.#@/=\\，期望失败，实际失败，pass
                输入空None，期望失败，实际失败，pass
                输入Power201，期望成功，实际成功，pass
                输入中英文，期望成功，实际成功，pass
                输入9999999999999999999999，期望失败，实际失败，pass
"""
data2 = {
'adress': "power201",
'agent': 134521278181376,
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
'customer': 134521334804481,
'downPrice': [{'endTime': 86400, 'id': 194, 'powerStation': 205, 'price': 1.2, 'startTime': 0}],
'eTotalToGrid': "0",
'eTotalToGridUnit': "kWh",
'eoutDaily': "0",
'eoutDailyUnit': "kWh",
'eoutMonth': "0",
'eoutMonthUnit': "kWh",
'gridActivePower': "0",
'gridActivePowerUnit': "kW",
'id': 205,
'isShown': 1,
'latitude': "30",
'longitude': "120",
'monthProfit': "0",
'name': '*&%^\/',
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
'upPrice': [{'endTime': 86400, 'id': 196, 'powerStation': 205, 'price': 1.2, 'startTime': 0}],
'updateTime': 0,
'value': "Asia/Shanghai",
}
"""
downprice和upprice的结束时间为空，期望失败，实际失败，pass
            price输入空None，期望失败，实际接口返回失败，但后台数据库依然创建成功，pass.
            price输入字符串，期望失败，实际失败，pass
            price输入特殊字符，期望失败，实际失败，pass
            price输入999999999，pass
            price输入-9，pass
            starttime输入None，期望失败，实际接口返回失败，但后台数据库依然创建成功，pass
            starttime输入jkjkajd字符串，期望失败，实际失败，pass
            starttime至endtime不足86400，期望失败，实际成功，pass
            downprice中的powstation字段和id字段不一致，期望失败，实际成功，导致电价相关信息丢失，fail
            downprice中的id字段传入不存在的id，期望失败，实际成功，导致电价相关信息丢失，pass
            
            starttime至endtime超过86400，期望失败，实际失败，pass
            starttime大于endtime，期望失败，实际成功，pass
"""

data3 = {
'adress': "power201",
'agent': 134521278181376,
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
'customer': 134521334804481,
'downPrice': [{'endTime': 86400, 'id': 194, 'powerStation': 205, 'price': 9, 'startTime': 0}],
'eTotalToGrid': "0",
'eTotalToGridUnit': "kWh",
'eoutDaily': "0",
'eoutDailyUnit': "kWh",
'eoutMonth': "0",
'eoutMonthUnit': "kWh",
'gridActivePower': "0",
'gridActivePowerUnit': "kW",
'id': 205,
'isShown': 1,
'latitude': "30",
'longitude': "120",
'monthProfit': "0",
'name': 'power201',
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
'upPrice': [{'endTime': 86400, 'id': 197, 'powerStation': 205, 'price': 100, 'startTime': 0}],
'updateTime': 0,
'value': "Asia/Shanghai",
}
"""
timezone输入不存在的时区id，期望失败，实际失败，pass
        输入特殊字符，期望失败，实际失败，pass
        输入空None,期望失败，实际失败，pass
        输入负值-78，期望失败，实际失败，pass
"""
data4 = {
'adress': "power201",
'agent': 134521278181376,
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
'customer': 134521334804481,
'downPrice': [{'endTime': 86400, 'id': 194, 'powerStation': 205, 'price': 9, 'startTime': 0}],
'eTotalToGrid': "0",
'eTotalToGridUnit': "kWh",
'eoutDaily': "0",
'eoutDailyUnit': "kWh",
'eoutMonth': "0",
'eoutMonthUnit': "kWh",
'gridActivePower': "0",
'gridActivePowerUnit': "kW",
'id': 205,
'isShown': 1,
'latitude': "30",
'longitude': "120",
'monthProfit': "0",
'name': 'power201',
'position': "120,30",
'productSeries': None,
'productSeriesName': None,
'pvCapacity': "1000",
'pvCapacityUnit': "kWp",
'registrationTime': 1634798011000,
'status': 2,
'systemType': 1,
'systemTypeName': "光伏并网系统",
'timezone': -78,
'timezoneName': "(UTC+08:00)北京",
'todayProfit': "0",
'totalProfit': "0",
'upPrice': [{'endTime': 86400, 'id': 197, 'powerStation': 205, 'price': 100, 'startTime': 0}],
'updateTime': 0,
'value': "Asia/Shanghai",
}
"""
电站id，传入不存在的电站id，期望失败，实际失败，pass
        传入非法数值，期望失败，实际失败，pass
        传入字符串，期望失败，实际失败，pass
"""
data5 = {
'adress': "power201",
'agent': 134521278181376,
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
'customer': 134521334804481,
'downPrice': [{'endTime': 86400, 'id': 194, 'powerStation': 205, 'price': 10, 'startTime': 0}],
'eTotalToGrid': "0",
'eTotalToGridUnit': "kWh",
'eoutDaily': "0",
'eoutDailyUnit': "kWh",
'eoutMonth': "0",
'eoutMonthUnit': "kWh",
'gridActivePower': "0",
'gridActivePowerUnit': "kW",
'id': 205,
'isShown': 1,
'latitude': "30",
'longitude': "120",
'monthProfit': "0",
'name': 'power201',
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
'upPrice': [{'endTime': 86400, 'id': 197, 'powerStation': 205, 'price': 100, 'startTime': 0}],
'updateTime': 0,
'value': "Asia/Shanghai",
}
"""
systemTye输入不存在的系统类型，期望失败，实际失败，pass
        输入空None，期望失败，实际失败，pass
        输入字符串，期望失败，实际失败，pass
        输入负值-78，期望失败，实际成功，pass
        更改系统类型为0，期望失败，实际失败，pass
        
"""
data6 = {
'adress': "power201",
'agent': 134521278181376,
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
'customer': 134521334804481,
'downPrice': [{'endTime': 86400, 'id': 194, 'powerStation': 205, 'price': 10, 'startTime': 0}],
'eTotalToGrid': "0",
'eTotalToGridUnit': "kWh",
'eoutDaily': "0",
'eoutDailyUnit': "kWh",
'eoutMonth': "0",
'eoutMonthUnit': "kWh",
'gridActivePower': "0",
'gridActivePowerUnit': "kW",
'id': 205,
'isShown': 1,
'latitude': "30",
'longitude': "120",
'monthProfit': "0",
'name': 'power201',
'position': "120,30",
'productSeries': None,
'productSeriesName': None,
'pvCapacity': "1000",
'pvCapacityUnit': "kWp",
'registrationTime': 1634798011000,
'status': 2,
'systemType': 0,
'systemTypeName': "光伏并网系统",
'timezone': 94,
'timezoneName': "(UTC+08:00)北京",
'todayProfit': "0",
'totalProfit': "0",
'upPrice': [{'endTime': 86400, 'id': 197, 'powerStation': 205, 'price': 100, 'startTime': 0}],
'updateTime': 0,
'value': "Asia/Shanghai",
}

"""
currencyUnit字段输入不存在的币种，期望失败，实际失败，pass
                输入特殊字符，期望失败，实际失败，pass
                输入字符串，期望失败，实际失败，pass
                输入空None，期望失败，实际成功，pass
                输入负值-78，期望失败，实际失败，pass

"""
data7 = {
'adress': "power201",
'agent': 134521278181376,
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
'customer': 134521334804481,
'downPrice': [{'endTime': 86400, 'id': 194, 'powerStation': 205, 'price': 10, 'startTime': 0}],
'eTotalToGrid': "0",
'eTotalToGridUnit': "kWh",
'eoutDaily': "0",
'eoutDailyUnit': "kWh",
'eoutMonth': "0",
'eoutMonthUnit': "kWh",
'gridActivePower': "0",
'gridActivePowerUnit': "kW",
'id': 205,
'isShown': 1,
'latitude': "30",
'longitude': "120",
'monthProfit': "0",
'name': 'power201',
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
'upPrice': [{'endTime': 86400, 'id': 197, 'powerStation': 205, 'price': 8, 'startTime': 0}],
'updateTime': 0,
'value': "Asia/Shanghai",
}
"""
pvCapacity字段输入特殊字符，期望失败，实际成功，pass
        输入空，期望失败，实际接口返回失败，但数据库依然创建成功，pass
        输入字符串，期望失败，实际成功，pass
        输入负值-78，期望失败，实际成功，pass
        输入负值0，期望失败，实际成功，pass
        输入999999999999.9，期望失败，实际成功，pass
"""
data8\
    = {
'adress': "power201",
'agent': 134521278181376,
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
'customer': 134521334804481,
'downPrice': [{'endTime': 86400, 'id': 194, 'powerStation': 205, 'price': 10, 'startTime': 0}],
'eTotalToGrid': "0",
'eTotalToGridUnit': "kWh",
'eoutDaily': "0",
'eoutDailyUnit': "kWh",
'eoutMonth': "0",
'eoutMonthUnit': "kWh",
'gridActivePower': "0",
'gridActivePowerUnit': "kW",
'id': 205,
'isShown': 1,
'latitude': "30",
'longitude': "120",
'monthProfit': "0",
'name': 'power201',
'position': "120,30",
'productSeries': None,
'productSeriesName': None,
'pvCapacity': 100,
'pvCapacityUnit': "kWp",
'registrationTime': 1634798011000,
'status': 2,
'systemType': 1,
'systemTypeName': "光伏并网系统",
'timezone': 94,
'timezoneName': "(UTC+08:00)北京",
'todayProfit': "0",
'totalProfit': "0",
'upPrice': [{'endTime': 86400, 'id': 197, 'powerStation': 205, 'price': 8, 'startTime': 0}],
'updateTime': 0,
'value': "Asia/Shanghai",
}
header = {'Content-Type': 'application/json', 'authorization': token}
res = requests.post(url=url, json=data, headers = header)
print(res.json())
print(res.status_code)