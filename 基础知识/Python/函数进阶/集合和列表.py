# -*- coding: utf-8 -*-
# @Time :2021/7/6 10:44
# @Author : liufei
# @File :集合和列表.PY

"""
集合和字典都是用{}来表示的
集合是可变类型数据
集合是无序的
"""

# 创建集合
se = set()  # 空集合
print(type(se))
set_1 = {1, 3, 4}
set_2 = {1, 3, 2, 2, 4, 3, 1}  # 集合有自动去重的功能
print(set_2)

list_1 = [1, 2, 2, 2, 2]
print(list(set(list_1)))  # 先强制转化成集合，再强制转化成列表

set_1.add('liu_fei')  # 集合添加元素
set_1.remove('liu_fei')  # 集合删除元素
set_1.update({'百度', '京东', '淘宝'})  # 通过可迭代的数据类型，来整体添加集合元素
one = set_1.copy()
print(one)
set_1.clear()  # 清空集合元素
print(set_1)
