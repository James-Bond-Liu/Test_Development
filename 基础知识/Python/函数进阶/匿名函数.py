# -*- coding: utf-8 -*-
# @Time :2021/7/11 10:11
# @Author : liufei
# @File :匿名函数.PY

# 适用场景：简单的函数定义（只有一个表达式）
# 匿名函数
lambda a, b: a + b
# 函数调用一
res = lambda a, b: a + b
print(res(1, 2))
# 函数调用二，即用即释放
(lambda a, b: a + b)(1, 2)

# 实例
list1 = [1, 4, 5, 23, 44, 6, 456]
res2 = filter(lambda x: x < 10, list1)
print(list(res2))
