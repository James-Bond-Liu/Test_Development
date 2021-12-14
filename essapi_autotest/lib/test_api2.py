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
# from lib.get_testdata import GetRequestData
from lib.get_all_testdata2 import GetRequestData
import unittest
from conf.global_data import GlobalData
from lib.out_log import OutLog
from ddt import ddt, data
from lib.do_mysql import DoMysql
from lib.read_config import ReadConfig
import os

"""
此模块用于封装执行某个Excel文件下所有sheet表单的用例
将登录用例写在Excel文件中，先执行登录用例获取token
"""

logger = OutLog().out_log()
test_data = GetRequestData().get_request_data()
read_conf = ReadConfig()


@ddt
class TestApi(unittest.TestCase):
    #
    # def __init__(self, methodName, case_id, case_name, url, method,parameters, expected_result, actual_result,sheet_name, file_name):
    #     super(TestApi, self).__init__(methodName)
    #     self.case_id = case_id
    #     self.case_name = case_name
    #     self.url=url
    #     self.method =method
    #     self.parameters = parameters
    #     self.expected_result = expected_result
    #     self.actual_result = actual_result
    #     self.sheet_name = sheet_name
    #     self.file_name = file_name

    def setUp(self):
        pass

    @classmethod
    def setUpClass(cls):
        pass

    @data(*test_data)
    def test_api(self, item):
        compare_result = None

        if item['sql_before']:
            if item['path_info'].find('${customer_no}') !=-1:
                sql_result1 = \
                    DoMysql(eval(read_conf.readconfig('MYSQL_DB', item['database1']))).select(item['sql_before'])[0]
                setattr(GlobalData, 'customer_no', sql_result1)
            elif item['parameters'] is not None and item['parameters'].find('${code}') != -1:
                sql_result1 = \
                DoMysql(eval(read_conf.readconfig('MYSQL_DB', item['database1']))).select(item['sql_before'])[0]
                setattr(GlobalData, 'code', sql_result1)
            elif item['path_info'].find('${organization_id}') != -1:
                sql_result1 = \
                    DoMysql(eval(read_conf.readconfig('MYSQL_DB', item['database1']))).select(item['sql_before'])[0]
                setattr(GlobalData, 'organization_id', sql_result1)

            if item['path_info'].find('${customer_no}') !=-1:
                item['path_info'] = item['path_info'].replace('${customer_no}', str(getattr(GlobalData, 'customer_no')))
            elif item['parameters'] is not None and item['parameters'].find('${code}') != -1:
                item['parameters'] = item['parameters'].replace('${code}', str(getattr(GlobalData, 'code')))
            elif item['path_info'].find('${organization_id}') != -1:
                item['path_info'] = item['path_info'].replace('${organization_id}', str(getattr(GlobalData, 'organization_id')))
            elif item['parameters'] is not None and item['parameters'].find('${organization_id}') != -1:
                item['parameters'] = item['parameters'].replace('${organization_id}', str(getattr(GlobalData, 'organization_id')))
        headers = {'Content-Type': 'application/json', 'authorization': getattr(GlobalData, 'token')}
        cookies = getattr(GlobalData, 'cookies')
        logger.info('测试用例{}，开始请求接口'.format(item['case_name']))
        if item['parameters'] is not None:
            res = HttpRequest().http_request(item['path_info'], eval(item['parameters']), item['method'], headers=headers,
                                             cookies=cookies)
            logger.info('测试用例{}，接口请求完成'.format(item['case_name']))
        elif item['parameters'] is None:
            res = HttpRequest().http_request(item['path_info'], item['parameters'], item['method'],
                                             headers=headers,
                                             cookies=cookies)
            logger.info('测试用例{}，接口请求完成'.format(item['case_name']))
        if res.json().get('data'):
            if 'access_token' in res.json()['data']:
                token = 'Bearer ' + res.json()['data']['access_token']
                setattr(GlobalData, 'token', token)
                logger.debug('测试用例{}响应报文携带token{}'.format(item['case_name'], token))
            else:
                logger.debug('测试用例{}响应报文没有携带token'.format(item['case_name']))
        else:
            logger.debug('测试用例{}响应报文没有key-"data"'.format(item['case_name']))
        if res.cookies:
            setattr(GlobalData, 'cookies', res.cookies)
            logger.debug('测试用例{}响应报文携带cookie{}'.format(item['case_name'], res.cookies))
        else:
            logger.debug('测试用例{}响应报文未携带cookie'.format(item['case_name']))
        try:
            self.assertEqual(res.status_code, 200)
            logger.info('测试用例{}响应状态码200，断言通过'.format(item['case_name']))
            self.assertEqual(res.json()['msg_code'], item['expected_result'])
            logger.info('测试用例{}响应报文operate.success，断言通过'.format(item['case_name']))
            if item['sql_result2'] is not None:
                logger.info('测试用例{}需要查询数据库'.format(item['case_name']))
                con = ReadConfig().readconfig('MYSQL_DB', item['database2'])
                sql_result2 = DoMysql(eval(con)).select(item['sql_after'])
                logger.info('测试用例{}查询数据库结果为{}'.format(item['case_name'], sql_result2[0]))
                if sql_result2[0] == item['sql_result2']:
                    compare_result = 'Pass'
                else:
                    compare_result = 'Failed'
                    logger.error('测试用例{}数据库比对结果失败'.format(item['case_name']))
            else:
                logger.info('测试用例{}不需要查询数据库'.format(item['case_name']))
                compare_result = 'Pass'

            # logger.info('测试用例{}断言通过，测试结果为{}'.format(item['case_name'], compare_result))
        except Exception as e:
            compare_result = 'Failed'
            logger.error('测试用例{}断言失败，报错{}'.format(item['case_name'], e))
            raise e
        finally:
            try:
                logger.info('在Excel中写入用例响应报文')
                file_name = os.path.join(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0], 'data',
                                         item['file_name'])  # 将item['file_name]拼接成一个绝对路径
                GetRequestData().write_back(file_name, item['sheet_name'], item['case_id'] + 1, 9, str(res.json()))
                logger.info('在Excel中写入用例的断言结果')
                GetRequestData().write_back(file_name, item['sheet_name'], item['case_id'] + 1, 13, compare_result)
            except Exception as e:
                logger.error('在Excel中写入数据失败，报错{}'.format(e))
                raise e

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
