# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ess_api
# @File     :修改密码
# @Date     :2021/11/15 9:55
# @Author   :LiuFei
# @Email    :fei.liu@hxgroup.com
# @Software :PyCharm
-------------------------------------------------
"""

import requests
url = "http://172.30.14.239:8080/ctrller-manager/productType/deleteDeviceLibrary?id="
token = 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJjdXN0b21lci0wMDAwMDAwMDAwMDAwMDAiLCJjb2RlIjoibmJwIiwidG9rZW5JZCI6MTM4MzMwMTUwODQ2NDY0LCJleHAiOjE2NDAzOTkzNTYsImlhdCI6MTYzNzgwNzM1Niwib3duZXJfdHlwZSI6Im9wZXJhdG9yIiwibG9jYWwiOiJ6aC1DTiJ9.G9QunolqbrM7BvRy29R1RBi18uURVmdjunVPEQBPPPcjyw0VCz7TR45hQj5428KGykwFURkccCsXdFYLC5DvTg'

header = {"Content-Type": "application/json", "authorization": token}
res = requests.post(url=url,headers = header)
print(res.json())
print(res.status_code)





