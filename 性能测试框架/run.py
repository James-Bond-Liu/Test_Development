# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ESS_API
# @File     :run
# @Date     :2021/8/17 13:39
# @Author   :LiuFei
# @Email    :fei.liu@hxgroup.com
# @Software :PyCharm
-------------------------------------------------
"""
import time
import unittest
from lib.out_log import OutLog
import datetime
from lib.test_api import TestApi
from template import HTMLTestRunnerNew
from conf.project_path import *

# log_path = os.path.join(project_path, 'log', 'running_log.log')
# html_report_path = os.path.join(project_path, 'report', 'test_report.html')
# txt_report_path =

class Run():

    def clean_up(self):
        # 日志、测试报告等文件清理
        if os.path.exists(log_path):
            with open(log_path, 'w') as file1:
                file1.truncate(0)
        if os.path.exists(html_report_path):
            with open(html_report_path, 'wb') as file2:
                file2.truncate(0)
        if os.path.exists(txt_report_path):
            with open(txt_report_path, 'w') as file3:
                file3.truncate(0)
        time.sleep(3)

    def run(self, formwork='html'):
        self.clean_up()
        logger = OutLog().out_log()
        # 执行测试用例
        start_time = datetime.datetime.now()
        logger.info('开始执行接口测试，开始时间{}'.format(start_time))

        suite = unittest.TestSuite()
        loader = unittest.TestLoader()
        suite.addTest(loader.loadTestsFromTestCase(TestApi))
        if formwork.lower() == 'txt':
            logger.info('测试报告为TXT格式')
            with open(file=txt_report_path, mode='w+') as file:
                runner = unittest.TextTestRunner(stream=file, verbosity=2)
                runner.run(suite)
        elif formwork.lower() == 'console':
            runner = unittest.TextTestRunner()
            runner.run(suite)
        else:
            logger.info('测试报告为HTML格式')
            with open(file=html_report_path, mode='wb') as file:
                runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title='测试报告',
                                                          description='HESS户用储能后端接口自动化测试报告')
                runner.run(suite)
        end_time = datetime.datetime.now()
        time_consuming = ((end_time - start_time).seconds) / 60  # 共耗时
        logger.info('完成接口测试，结束时间{}，共耗时{}'.format(end_time, end_time - start_time))


if __name__ == '__main__':
    Run().run()
