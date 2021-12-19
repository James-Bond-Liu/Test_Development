# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ESS_API
# @File     :login
# @Date     :2021/8/13 10:26
# @Author   :Liu Fei
# @Software :PyCharm
-------------------------------------------------
"""
import requests
from 性能测试框架.lib.out_log import OutLog

logger = OutLog().out_log()
class HttpRequest():

    def http_request(self,url, data, http_method, headers, cookies=None):
        try:
            if http_method.upper() == 'GET':
                res = requests.get(url=url, params=data, headers=headers, cookies=cookies)

            elif http_method.upper() == 'POST':
                res = requests.post(url=url, json=data, headers=headers, cookies=cookies)

            elif http_method.upper() == 'DELETE':
                res = requests.delete(url=url, params=data, headers=headers, cookies=cookies)

            elif http_method.upper() == 'PUT':
                res = requests.put(url=url, json=data, headers=headers, cookies=cookies)

            else:
                logger.error('输入的请求方法不正确')
        except Exception as e:
            logger.error("请求出错了{0}".format(e))
            raise e
        return res

if __name__ == '__main__':
    import json

    data = {'username': 'admin', 'passwd': 'Hx.123456'}
    data = {'login_account':'admin', 'password':'Hx.123456', 'account_type':'email', 'language':'en'}
    res = requests.post(url='http://172.30.12.227:8088/boring-customer/login/customer', json=data)
    print(res.status_code)
    print(res.json())
    print(res.text)