# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ess_api
# @File     :加密
# @Date     :2021/11/15 9:52
# @Author   :LiuFei
# @Email    :fei.liu@hxgroup.com
# @Software :PyCharm
-------------------------------------------------
"""
# import hashlib
#
# s = 'Ltk123456'
# print(len(s))
# md = hashlib.md5()
# print(s)
# md.update(s.encode(encoding='utf-8'))
# print(md.hexdigest())
#
# print('站'*65)
# print('b'*65)

import time
from datetime import datetime

time_str = '2019-11-24 12:12:12'
de = time.strptime(time_str, '%Y-%m-%d %H:%M:%S')
print(int(time.mktime(de)))

print(datetime.fromtimestamp(1574568732))

{'deviceTypeCode': 1,
'inverterSn': "11234567891",
'org': 0,
'productTypeCode': 9}

("hess", "deviceId" "select count(*) from scada_device_library where inverter_sn='11234567891' and is_delete=0;")

{0: {'deviceTypeCode': 1, 'productTypeCode': 9, 'inverterSn': '11234567891', 'org': 0}}
a={'id': 9,
'snList': ["11234567891"]}

插入一个SN号
新增一个设备
增加一个SN号相同的设备
删除新增加的设备
不存在的code
code传入None
sn号传入None
sn号传入不存在
org为None
org为不存在的9999
typecode为None
typecode为不存在的
typecode为特殊字符
typecode为字符串
删除SN号
