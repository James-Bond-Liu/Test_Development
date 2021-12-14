# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ESS_API
# @File     :test_api
# @Date     :2021/8/16 16:15
# @Author   :LiuFei
# @Email    :fei.liu@hxgroup.com
# @Software :PyCharm
-------------------------------------------------
"""
from lib.http_request import HttpRequest
from lib.get_testdata弃用 import GetRequestData
from conf import project_path
import unittest
from conf.global_data import GlobalData
from lib.out_log import OutLog
from ddt import ddt, data
import requests

"""
1、此模块用于封装执行某个Excel文件下所有sheet表单的用例
2、讲登录请求封装在测试用例中，每个测试类执行前先执行登录请求从而获取token
"""


logger = OutLog().out_log()
test_data = GetRequestData(project_path.excel_data).get_request_data()
@ddt
class TestApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        res = requests.post(url='http://172.30.12.227:8088/boring-customer/login/customer',
                            json={"login_account": "admin", "password": "b71ba87da2b0ba25599c8173f4946430",
                                  "account_type": "email", "language": "en"})
        token = 'Bearer ' + res.json()['data']['access_token']
        setattr(GlobalData, 'token', token)



    @data(*test_data)
    def test_api(self, item):
        headers = {'Content-Type':'application/json', 'authorization': getattr(GlobalData,'token')}
        cookies = getattr(GlobalData, 'cookies')
        logger.info('接口开始运行')
        res = HttpRequest().http_request(item['url'], eval(item['parameters']), item['method'], headers=headers, cookies=cookies)
        logger.info('接口运行完成')
        # token = res.json()['data']['access_token']
        # setattr(GlobalData, 'token', token)
        try:
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.json()['msg_code'], item['expected_result'])
            compare_result = 'Pass'
        except Exception as e:
            compare_result = 'Failed'
            logger.error('执行用例{}，报错{}'.format(item['case_name'], e))
            raise e
        finally:
            logger.info('写入用例请求的实际结果')
            GetRequestData(project_path.excel_data).write_back(item['sheet_name'],item['case_id']+1, 7, str(res.json()))
            logger.info('写入用例的执行结果')
            GetRequestData(project_path.excel_data).write_back(item['sheet_name'], item['case_id'] + 1, 8, compare_result)
        # if res.json()['data']['access_token']:
        # token = res.json()['data']['access_token']
        #
        # setattr(GlobalData, 'token', token)
        # elif res.cookies:
        #     setattr(GlobalData, 'cookies', res.cookies)



    def tearDown(self):
        pass

    # def tearDownClass(cls):
    #     pass
