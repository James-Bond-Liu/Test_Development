# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ess_api
# @File     :toBadmin登录
# @Date     :2021/10/8 13:52
# @Author   :LiuFei
# @Email    :fei.liu@hxgroup.com
# @Software :PyCharm
-------------------------------------------------
"""

import requests
data = {
"account_type": "email",
"language": "en",
"login_account": "test201",
"password": "ab3a7e4cf5f8d34673809b7c1068e496"
}
url = "http://172.30.14.239:8080/nbp/login/customer"
res = requests.post(url=url, json=data)
print(res.status_code)
print(res.json())