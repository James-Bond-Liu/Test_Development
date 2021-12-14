# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ess_api
# @File     :ctrller-manager-powerstation-insert
# @Date     :2021/11/4 10:12
# @Author   :LiuFei
# @Email    :fei.liu@hxgroup.com
# @Software :PyCharm
-------------------------------------------------
"""
import requests
url = 'http://172.30.14.239:8080/ctrller-manager/powerstation/insert'
token = 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJjdXN0b21lci0xMHpyYjRrY2F6dW8iLCJjb2RlIjoibmJwIiwidG9rZW5JZCI6MTM1MjU1MDMxODIwMjg4LCJleHAiOjE2Mzg5MzMwMjUsImlhdCI6MTYzNjM0MTAyNSwib3duZXJfdHlwZSI6ImN1c3RvbWVyIiwibG9jYWwiOiJlbiJ9._DSDmWgovchST3S--axHqcYA3lzuR-MsAOF6zyigJjOmMfFLULrrW9gq2PevC7t-8o0epNbdMyMoJfGNuYjqxQ'

"""
电站名称name字段输入特殊字符_-,.#@/=\\，期望成功，实际成功，pass
                输入空None，期望失败，实际失败，pass
                输入Power201，期望成功，实际成功，pass
                输入中英文，期望成功，实际成功，pass
                输入9999999999999999999999，期望失败，实际成功，pass
"""
data1 = {
'adress': "power201",
'agent': 134521278181376,
'chargingType': None,
'countryValue': "CN",
'currencyUnit': 3,
'downPrice': [{'price': "1.2", 'startTime': 0, 'endTime': 86400}],
'installer': None,
'installerName': "",
'isShown': 1,
'latitude': "30",
'longitude': "120",
'name': '_-,.#@/=\\',
'position': "",
'pvCapacity': 1000,
'systemType': 1,
'timezone': 94,
'timezoneName': "",
'upPrice': [{'price': "1.2", 'startTime': 0, 'endTime': 86400}]
}



"""
安装商agnet字段输入不存在的id，接口返回报错，但后台数据库依然创建成功，pass
            输入空None，期望失败，实际成功，pass
            输入字符串，期望失败，实际失败，pass
            输入特殊字符，期望失败，实际失败，pass
"""
data2 = {
'adress': "power201",
'agent': None,
'chargingType': None,
'countryValue': "CN",
'currencyUnit': 3,
'downPrice': [{'price': "1.2", 'startTime': 0, 'endTime': 86400}],
'installer': None,
'installerName': "",
'isShown': 1,
'latitude': "30",
'longitude': "120",
'name': "power202",
'position': "",
'pvCapacity': 1000,
'systemType': 1,
'timezone': 94,
'timezoneName': "",
'upPrice': [{'price': "1.2", 'startTime': 0, 'endTime': 86400}]
}


"""
downprice和upprice的结束时间为空，期望失败，实际接口返回失败，但后台数据库依然创建成功，pass
            price输入空None，期望失败，实际接口返回失败，但后台数据库依然创建成功，pass.
            price输入字符串，期望失败，实际失败，pass
            price输入特殊字符，期望失败，实际失败，pass
            price输入999999999，pass
            price输入-9，pass
            starttime输入None，期望失败，实际接口返回失败，但后台数据库依然创建成功，pass
            starttime输入jkjkajd字符串，期望失败，实际失败，pass
            starttime至endtime不足86400，期望失败，实际成功，pass
            starttime至endtime超过86400，期望失败，实际成功，pass
            starttime大于endtime，期望失败，实际成功，pass
            downprice 由两个时间线组成，第二条时间线的starttime早于第一条时间线的endtime，期望失败，实际成功，pass
"""
data3 = {
'adress': "power201",
'agent': 134521278181376,
'chargingType': None,
'countryValue': "CN",
'currencyUnit': 3,
'downPrice': [{'price': "1.5", 'startTime': 0, 'endTime': 43200}],
'installer': None,
'installerName': "",
'isShown': 1,
'latitude': "30",
'longitude': "120",
'name': "power201",
'position': "",
'pvCapacity': 1000,
'systemType': 1,
'timezone': 94,
'timezoneName': "",
'upPrice': [{'price': "1.2", 'startTime': 0, 'endTime': 86400}]
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
'chargingType': None,
'countryValue': "CN",
'currencyUnit': 3,
'downPrice': [{'price': "1.2", 'startTime': 0, 'endTime': 86400}],
'installer': None,
'installerName': "",
'isShown': 1,
'latitude': "30",
'longitude': "120",
'name': "power201",
'position': "",
'pvCapacity': 1000,
'systemType': 1,
'timezone': 4984324,
'timezoneName': "",
'upPrice': [{'price': "1.2", 'startTime': 0, 'endTime': 86400}]
}
"""
psystemTye输入不存在的系统类型，期望失败，实际成功，pass
        输入空None，期望失败，实际成功，pass
        输入字符串，期望失败，实际失败，pass
        输入负值-78，期望失败，实际成功，pass
"""
data5 = {
'adress': "power201",
'agent': 134521278181376,
'chargingType': None,
'countryValue': "CN",
'currencyUnit': 3,
'downPrice': [{'price': "1.2", 'startTime': 0, 'endTime': 86400}],
'installer': None,
'installerName': "",
'isShown': 1,
'latitude': "30",
'longitude': "120",
'name': "power201",
'position': "",
'pvCapacity': 1000,
'systemType': None,
'timezone': 94,
'timezoneName': "",
'upPrice': [{'price': "1.2", 'startTime': 0, 'endTime': 86400}]
}
header = {'Content-Type': 'application/json', 'authorization': token}
"""
pvCapacity字段输入特殊字符，期望失败，实际成功，pass
        输入空，期望失败，实际接口返回失败，但数据库依然创建成功，pass
        输入字符串，期望失败，实际成功，pass
        输入负值-78，期望失败，实际成功，pass
        输入负值0，期望失败，实际成功，pass
        输入999999999999.9，期望失败，实际成功，pass
"""
data6 = {
'adress': "power201",
'agent': 135253345710080,
'chargingType': None,
'countryValue': "CN",
'currencyUnit': 3,
'downPrice': [{'price': "1.2", 'startTime': 0, 'endTime': 86400}],
'installer': None,
'installerName': "",
'isShown': 1,
'latitude': "30",
'longitude': "120",
'name': "power201",
'position': "",
'pvCapacity': 999999999999.9,
'systemType': 1,
'timezone': 94,
'timezoneName': "",
'upPrice': [{'price': "1.2", 'startTime': 0, 'endTime': 86400}]
}
"""
pvCapacity字段输入负数/999999999999.9，期望失败，实际成功，pass
"""
data7 = {
'adress': "power201",
'agent': 134521278181376,
'chargingType': None,
'countryValue': "CN",
'currencyUnit': 3,
'downPrice': [{'price': "1.2", 'startTime': 0, 'endTime': 86400}],
'installer': None,
'installerName': "",
'isShown': 1,
'latitude': "30",
'longitude': "120",
'name': "power201",
'position': "",
'pvCapacity': '999999999999.9',
'systemType': 1,
'timezone': 94,
'timezoneName': "",
'upPrice': [{'price': "1.2", 'startTime': 0, 'endTime': 86400}]
}
"""
    currencyUnit字段输入不存在的币种，期望失败，实际失败，pass
                输入特殊字符，期望失败，实际失败，pass
                输入字符串，期望失败，实际失败，pass
                输入空None，期望失败，实际成功，pass
                输入负值-78，期望失败，实际失败，pass
                
"""
data8 = {
'adress': "power201",
'agent': 134521278181376,
'chargingType': None,
'countryValue': None,
'currencyUnit': -78,
'downPrice': [{'price': "1.2", 'startTime': 0, 'endTime': 86400}],
'installer': None,
'installerName': "",
'isShown': 1,
'latitude': "30",
'longitude': "120",
'name': "power201",
'position': "",
'pvCapacity': '1000',
'systemType': 1,
'timezone': 94,
'timezoneName': "",
'upPrice': [{'price': "1.2", 'startTime': 0, 'endTime': 86400}]
}
res = requests.post(url=url, json=data, headers = header)
# print(res.json()['msg_code'])
print(res.json())
print(res.status_code)