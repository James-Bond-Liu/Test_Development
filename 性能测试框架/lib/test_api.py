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
import datetime
import numpy
from 性能测试框架.lib.http_request import HttpRequest

from 性能测试框架.lib.get_all_testdata import GetRequestData
import unittest
from 性能测试框架.conf.global_data import GlobalData
from 性能测试框架.lib.out_log import OutLog
from ddt import ddt, data
from 性能测试框架.lib.do_mysql import DoMysql
from 性能测试框架.lib.read_config import ReadConfig
import os
from 性能测试框架.lib.do_regx import DoRegx
from time import sleep
from multiprocessing import Process, Pool, Manager

logger = OutLog().out_log()
test_data = GetRequestData().get_request_data()

response_time = []


class TestApi():

    def work(self, q, data):
        start_time = datetime.datetime.now()
        token = 'Bearer '+q.get_nowait()
        while True:
            headers = {'Content-Type': 'application/json', 'authorization': token}
            cookies = getattr(GlobalData, 'cookies')
            res = HttpRequest().http_request(data['path_info'], data['paramters'], data['method'], headers, cookies)
            res_time = res.elapsed.total_seconds()
            response_time.append(res_time)
            if res.json().get('data'):
                if 'access_token' in res.json()['data']:
                    token = 'Bearer ' + res.json()['data']['access_token']
                    q.put_nowait(token)
                    # setattr(GlobalData, 'token', token)
                    logger.debug('测试用例{}响应报文返回token{}'.format(data['case_name'],token))
                else:
                    logger.debug('测试用例{}响应报文没有携带token'.format(data['case_name']))
            try:
                if res.status_code == '200' and res.json()['msg_code'] == 'operate success':
                    compare_result = 'Pass'
                    GetRequestData().write_back(data['file_name'], data['case_id'] + 1, 8, compare_result)

                elif res.json()['msg_code'] != 'operate success':
                    compare_result = 'Failed'
                    GetRequestData().write_back(data['file_name'], data['case_id'] + 1, 8, compare_result)

                elif res.status_code != 200:
                    compare_result = 'Failed'
                    GetRequestData().write_back(data['file_name'], data['case_id'] + 1, 8, compare_result)

            finally:
                GetRequestData().write_back(data['file_name'], data['case_id'] + 1, 8, str(res.json()))

            end_time = datetime.datetime.now()
            time = (end_time - start_time).seconds
            if time == 1800:
                break

        findal_time = sorted(response_time)
        average_time = numpy.mean(findal_time)
        max_time = findal_time[-1]
        min_time = findal_time[0]
        GetRequestData().write_back(data['file_name'], data['case_id'] + 1, '**', min_time)
        GetRequestData().write_back(data['file_name'], data['case_id'] + 1, '**', max_time)
        GetRequestData().write_back(data['file_name'], data['case_id'] + 1, '**', average_time)

    pool = Pool(30)
    q = Manager().Queue()
    token = None
    q.put_nowait(token)
    for i in test_data:
        pool.apply_async(work,q,i)
    pool.close()

    pool.join()


@ddt
class TestApi2(unittest.TestCase):

    def setUp(self):
        pass

    @classmethod
    def setUpClass(cls):
        pass

    @data(*test_data)
    def test_api(self, item):
        while True:
            start_time = datetime.datetime.now()

            compare_result = None

            if item['sql_before'] is not None:
                item['sql_before'] = DoRegx().do_regx(item['sql_before'])
                item['sql_before'] = eval(item['sql_before'])
                result1 = \
                    DoMysql(eval(ReadConfig().readconfig('MYSQL_DB', item['sql_before'][0]))).select(
                        item['sql_before'][2])[
                        0]
                setattr(GlobalData, item['sql_before'][1], result1)
                logger.debug(
                    f'测试用例---{item["case_name"]}的sql_before不为空，GlobalData{item["sql_before"][1]}={getattr(GlobalData, item["sql_before"][1])}')
            if item['parameters'] is not None:
                item['parameters'] = DoRegx().do_regx(item['parameters'])
                logger.debug(f'测试用例---{item["case_name"]}的parameters不为空')

            item['path_info'] = DoRegx().do_regx(item['path_info'])

            headers = {'Content-Type': 'application/json', 'authorization': getattr(GlobalData, 'token')}
            cookies = getattr(GlobalData, 'cookies')
            logger.info('**********测试用例{}，开始请求接口**********'.format(item['case_name']))
            if item['parameters'] is not None:
                logger.debug(f"测试用例---{item['case_name']}的请求地址为{item['path_info']}")
                logger.debug(f'测试用例---{item["case_name"]}的请求参数为{item["parameters"]}')
                res = HttpRequest().http_request(item['path_info'], eval(item['parameters']), item['method'],
                                                 headers=headers,
                                                 cookies=cookies)
                logger.info('**********测试用例{}，接口请求完成**********'.format(item['case_name']))
                logger.debug(f"测试用例---{item['case_name']}传入的请求头为{res.request.headers}")
            elif item['parameters'] is None:
                logger.debug(f"测试用例---{item['case_name']}的请求地址为{item['path_info']}")
                logger.debug(f'测试用例---{item["case_name"]}的请求参数为{item["parameters"]}')
                logger.info('**********测试用例{}，开始请求接口**********'.format(item['case_name']))
                res = HttpRequest().http_request(item['path_info'], item['parameters'], item['method'],
                                                 headers=headers,
                                                 cookies=cookies)
                logger.info('**********测试用例{}，接口请求完成**********'.format(item['case_name']))
                logger.debug(f"测试用例---{item['case_name']}发起请求的header为{res.request.headers}")
            if res.json().get('data'):
                if 'access_token' in res.json()['data']:
                    token = 'Bearer ' + res.json()['data']['access_token']
                    setattr(GlobalData, 'token', token)
                    logger.debug('测试用例---{}响应报文返回token{}'.format(item['case_name'], token))
                else:
                    logger.debug('测试用例---{}响应报文没有返回token'.format(item['case_name']))
            else:
                logger.debug('测试用例---{}响应报文没有【data2】字段'.format(item['case_name']))
            if res.cookies:
                setattr(GlobalData, 'cookies', res.cookies)
                logger.debug('测试用例---{}响应报文携带cookie{}'.format(item['case_name'], res.cookies))
            else:
                logger.debug('测试用例---{}响应报文未携带cookie'.format(item['case_name']))
            try:
                self.assertEqual(res.status_code, item['expect_status_code'])
                logger.info('测试用例---{}status_code为{}校验通过'.format(item['case_name'], res.status_code))
                logger.info(f"测试用例---{item['case_name']}的响应报文为{res.json()}")
                if res.status_code == 400:
                    self.assertEqual(res.json()['error'], item['request_expect_result'])
                    logger.info('测试用例---{}is bad request'.format(item['case_name'], res.json()['error']))
                elif res.status_code == 500:
                    self.assertEqual(res.json()['error'], item['request_expect_result'])
                    logger.info('测试用例---{}Internal Server Error'.format(item['case_name'], res.json()['error']))
                elif res.status_code == 200:
                    self.assertEqual(res.json()['msg_code'], item['request_expect_result'])
                    logger.info('测试用例---{}msg_code为{}'.format(item['case_name'], res.json()['msg_code']))

                if item['sql_after'] is not None:
                    item['sql_after'] = DoRegx().do_regx(item['sql_after'])
                    item['sql_after'] = eval(item['sql_after'])
                    result2 = \
                        DoMysql(eval(ReadConfig().readconfig('MYSQL_DB', item['sql_after'][0]))).select(
                            item['sql_after'][2])[0]
                    setattr(GlobalData, item['sql_after'][1], result2)
                    logger.debug(
                        f'测试用例---{item["case_name"]}的sql_after不为空，GlobalData{item["sql_after"][1]}={getattr(GlobalData, item["sql_after"][1])}')

                if item['database_compare_sql'] is not None:
                    item['database_compare_sql'] = DoRegx().do_regx(item['database_compare_sql'])
                    logger.debug(f'测试用例---{item["case_name"]}需要进行数据库校验，校验sql为{item["database_compare_sql"]}')
                    item['database_compare_sql'] = eval(item['database_compare_sql'])
                    con = ReadConfig().readconfig('MYSQL_DB', item['database_compare_sql'][0])
                    database_actual_result = DoMysql(eval(con)).select(item['database_compare_sql'][1])[0]
                    logger.debug('测试用例---{}查询数据库结果为{}，期望结果为{}'.format(item['case_name'], database_actual_result,
                                                                      item['database_expect_result']))
                    if database_actual_result == item['database_expect_result']:
                        compare_result = 'Pass'
                        logger.info(
                            f'{item["file_name"]}--{item["sheet_name"]}---测试用例---{item["case_name"]}断言结果为{compare_result}')
                    else:
                        compare_result = 'Failed'
                        logger.error(
                            f'{item["file_name"]}--{item["sheet_name"]}---测试用例---{item["case_name"]}断言结果为{compare_result}')
                else:
                    compare_result = 'Pass'
                    logger.info(
                        f'{item["file_name"]}--{item["sheet_name"]}---测试用例---{item["case_name"]}断言结果为{compare_result}')

            except Exception as e:
                compare_result = 'Failed'
                logger.error(
                    '{}---{}---测试用例---{}断言过程报错{}'.format(item['file_name'], item['sheet_name'], item['case_name'], e))
                raise e

            finally:
                try:
                    file_name = os.path.join(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0], 'data2',
                                             item['file_name'])  # 将item['file_name]拼接成一个绝对路径

                    GetRequestData().write_back(file_name, item['sheet_name'], item['case_id'] + 1, 8, str(res.json()))
                    logger.info(f'Excel中写入用例---{item["case_name"]}响应报文{res.json()}')

                    GetRequestData().write_back(file_name, item['sheet_name'], item['case_id'] + 1, 13, compare_result)
                    logger.debug(f'Excel中写入用例---{item["case_name"]}的断言结果{compare_result}')
                except Exception as e:
                    logger.error('在Excel中写入数据失败，报错{}'.format(e))
                    raise e

            end_time = datetime.datetime.now()
            total_time = (end_time - start_time).seconds()
            if total_time == 1800:
                break

    def tearDown(self):
        sleep(1)

    @classmethod
    def tearDownClass(cls):
        pass
