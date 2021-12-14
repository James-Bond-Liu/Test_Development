# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ESS_API
# @File     :do_mysql
# @Date     :2021/8/13 11:07
# @Author   :Liu Fei
# @Software :PyCharm
-------------------------------------------------
"""
import pymysql
from lib.out_log import OutLog
from conf.project_path import *

logger = OutLog().out_log()
class DoMysql():
    """封装数据库的相关操作"""

    def __init__(self, db_info):  # db_info数据库的连接信息必须以字典形式传入
        self.link = pymysql.connect(**db_info)
        self.cursor = self.link.cursor()

    def select(self, sql):  # 查询操作
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            self.cursor.close()
            self.link.close()
            return result
        except Exception as e:
            logger.error('数据库查询失败，报错{}'.format(e))

    def insert(self, sql):  # 插入操作
        try:
            self.cursor.execute(sql)
            self.link.commit()
            self.cursor.close()
            self.link.close()
        except Exception as e:
            self.link.rollback()
            logger.error('数据库插入失败，报错{}'.format(e))

    def update(self, sql):
        try:
            self.cursor.execute(sql)
            self.link.commit()
            self.cursor.close()
            self.link.close()
        except Exception as e:
            self.link.rollback()
            logger.error('数据库更改失败，报错{}'.format(e))

    def delete(self, sql):
        try:
            self.cursor.execute(sql)
            self.link.commit()
            self.cursor.close()
            self.link.close()
        except Exception as e:
            self.link.rollback()
            logger.error('数据库删除失败，报错{}'.format(e))



    # def do_db(self, sql, stat = 'all'):
    #     self.cursor.execute(sql)
    #     try:
    #         if stat == 'all':
    #             res = self.cursor.fetchall()  # 多条数据，列表嵌套元祖
    #         elif stat == 1:
    #             res = self.cursor.fetone()  # 一条数据，元祖
    #         else:
    #             logger.error('stat模式只能为1或者all')
    #         self.cursor.close()
    #         self.link.close()
    #         return res
    #     except Exception as e:
    #         logger.error(e)
    #         raise e

if __name__ == '__main__':
    from lib.read_config import ReadConfig
    con = ReadConfig().readconfig('MYSQL_DB', 'uap_2c')
    sql = 'select customer_no from nbp_customer_profile where login_account = "test003";'
    sql1 = 'select count(*) from nbp_customer_profile where login_account = "test003";'
    d = DoMysql(eval(con)).select(sql1)
    print(d)

    print(d)
    if d is None:
        print('liufei')
    else:
        print('python')