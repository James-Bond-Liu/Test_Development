import requests

url1 = "http://172.30.14.239:8080/ctrller-manager/i18n/sendCode"
token = None
header = {"Content-Type": "application/json", "authorization": token}
data ={"receiver": "test301@qq.com"}

res1 = requests.post(url=url1, json=data, headers = header)
print(res1.status_code)
print(res1.json())

url2 = "http://172.30.14.239:8080/nbp/customer/register"
token = None
header = {"Content-Type": "application/json", "authorization": token}
data ={"country_id": 45,
"email": "test301@qq.com",
"login_account": "test301",
"mobile": "",
"name": "",
"password": "b71ba87da2b0ba25599c8173f4946430",
"register_type": 1,
"telephone": "",
"verify_code": "123456"}

res2 = requests.post(url=url2, json=data, headers = header)
print(res2.status_code)
print(res2.json())
print(res2.elapsed.total_seconds())
# 117803


{"collectorSn": None,
"filterCountry": None,
"filterSn": None,
"filterStationId": [323],
"filterStatus": None,
"filterTime": [],
"filterVersion": None,
"filterWorkStatus": None,
"pageSize": 50,
"productTypeList": [],
"start": 1,
"systemType": None}

('uap_2c', 'select count(*) from nbp_operator where name="genAdmin301" and state="normal" and id = ${genAdminId};')