# -*- coding: utf-8 -*-
# @Time :2021/7/11 10:28
# @Author : liufei
# @File :偏函数.PY

from functools import partial

# 过滤如下列表小于10的数据
list1 = [1, 4, 5, 23, 44, 6, 456]
list2 = [1, 4, 5, 23, 44, 6, 456]
list3 = [1, 4, 5, 23, 44, 6, 456]

# 实现方法一
res1 = filter(lambda x: x < 10, list1)
res2 = filter(lambda x: x < 10, list1)
res3 = filter(lambda x: x < 10, list1)

# 实现方法二
# 从方法一中发现参数“lambda x: x < 10”,是固定的，后面的参数是需要变化的。利用偏函数固定一部分参数简化。
# partial(函数，参数1，参数2，....)
func1 = partial(filter, lambda x: x < 10)
res1_ = func1(list1)
res2_ = func1(list2)
res3_ = func1(list3)
