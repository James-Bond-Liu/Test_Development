# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ESS_API
# @File     :do_redis
# @Date     :2021/8/19 10:27
# @Author   :LiuFei
# @Email    :fei.liu@hxgroup.com
# @Software :PyCharm
-------------------------------------------------
"""
import redis


# redis = redis.Redis(host='172.30.12.227', port=6379,db=9, password=123456)

pool =redis.ConnectionPool(host='172.30.12.227', port=6379,db=9, password=123456, decode_responses=True)
redis = redis.StrictRedis(connection_pool=pool)
print(redis.randomkey())
print(redis.exists('channel:1000202106240624:timezone'))
print(redis.keys('c*'))
print(redis.get('channel:2113-59430897D:timezone'))
print(redis.type('channel:2113-59430897D:timezone'))
redis.set()