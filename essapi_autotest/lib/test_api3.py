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
from lib.do_regx import DoRegx
from time import sleep

"""
此模块用于封装执行某个Excel文件下所有sheet表单的用例
将登录用例写在Excel文件中，先执行登录用例获取token
"""

logger = OutLog().out_log()
test_data = GetRequestData().get_request_data()

@ddt
class TestApi(unittest.TestCase):

    def setUp(self):
        pass

    @classmethod
    def setUpClass(cls):
        pass

    @data(*test_data)
    def test_api(self, item):
        compare_result = None

        if item['sql_before'] is not None:
            item['sql_before'] = eval(item['sql_before'])
            result1 = DoMysql(eval(ReadConfig().readconfig('MYSQL_DB', item['sql_before'][0]))).select(item['sql_before'][2])[0]
            setattr(GlobalData, item['sql_before'][1], result1)
        if item['parameters'] is not None:
            item['parameters'] = DoRegx().do_regx(item['parameters'])

        item['path_info'] = DoRegx().do_regx(item['path_info'])

        headers = {'Content-Type': 'application/json', 'authorization': getattr(GlobalData, 'token')}
        cookies = getattr(GlobalData, 'cookies')
        logger.info('测试用例{}，开始请求接口'.format(item['case_name']))
        if item['parameters'] is not None:
            logger.debug(f"测试用例{item['case_name']}的请求地址为{item['path_info']}")
            logger.debug(f'测试用例{item["case_name"]}的请求参数为{item["parameters"]}')
            res = HttpRequest().http_request(item['path_info'], eval(item['parameters']), item['method'], headers=headers,
                                             cookies=cookies)
            logger.info('测试用例{}，接口请求完成'.format(item['case_name']))
        elif item['parameters'] is None:
            logger.debug(f"测试用例{item['case_name']}的请求地址为{item['path_info']}")
            logger.debug(f'测试用例{item["case_name"]}的请求参数为{item["parameters"]}')
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
            self.assertEqual(res.json()['msg_code'], item['request_expect_result'])
            logger.info('测试用例{}响应报文operate.success，断言通过'.format(item['case_name']))
            if item['sql_after'] is not None:
                item['sql_after'] = eval(item['sql_after'])
                result2 = DoMysql(eval(ReadConfig().readconfig('MYSQL_DB', item['sql_after'][0]))).select(item['sql_after'][2])[0]
                logger.debug(f'*****{result2}')
                setattr(GlobalData, item['sql_after'][1], result2)
                logger.debug(f'测试用例{item["case_name"]}sql查询{item["sql_after"][1]}结果是{getattr(GlobalData, item["sql_after"][1])}')
                logger.info('测试用例{}执行完成后查询数据库{}的结果为{}'.format(item['case_name'], item['sql_after'][1], result2))
                logger.debug('***********{}'.format(getattr(GlobalData, 'customer_id')))

            if item['database_compare_sql'] is not None:
                item['database_compare_sql'] = DoRegx().do_regx(item['database_compare_sql'])
                logger.debug(f'测试用例{item["case_name"]}需要进行数据库校验，校验sql为{item["database_compare_sql"]}')
                item['database_compare_sql'] = eval(item['database_compare_sql'])
                # logger.info('测试用例{}需要和数据库作比对'.format(item['case_name']))
                con = ReadConfig().readconfig('MYSQL_DB', item['database_compare_sql'][0])
                database_actual_result = DoMysql(eval(con)).select(item['database_compare_sql'][1])[0]
                logger.info('测试用例{}校验数据库结果为{}'.format(item['case_name'], database_actual_result))
                if database_actual_result == item['database_expect_result']:
                    compare_result = 'Pass'
                    logger.info(f'测试用例{item["case_name"]}校验数据库比对结果为{compare_result}')
                else:
                    compare_result = 'Failed'
                    logger.error(f'测试用例{item["case_name"]}校验数据库比对结果为{compare_result}')
            else:
                logger.info(f'测试用例{item["case_name"]}不需要进行数据库校验')
                compare_result = 'Pass'

        except Exception as e:
            compare_result = 'Failed'
            logger.error('测试用例{}断言失败，报错{}'.format(item['case_name'], e))
            raise e
        finally:
            try:
                logger.info('在Excel中写入用例响应报文')
                file_name = os.path.join(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0], 'data',
                                         item['file_name'])  # 将item['file_name]拼接成一个绝对路径
                GetRequestData().write_back(file_name, item['sheet_name'], item['case_id'] + 1, 8, str(res.json()))
                logger.info('在Excel中写入用例的断言结果')
                GetRequestData().write_back(file_name, item['sheet_name'], item['case_id'] + 1, 12, compare_result)
            except Exception as e:
                logger.error('在Excel中写入数据失败，报错{}'.format(e))
                raise e

    def tearDown(self):
        sleep(1)

    @classmethod
    def tearDownClass(cls):
        pass
