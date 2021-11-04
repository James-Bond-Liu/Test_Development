# -*- coding: utf-8 -*-
# @Time :2021/7/11 10:52
# @Author : liufei
# @File :三目运算符.PY

# 常运用在简单的if/else语句中
# 语法格式：为真时的结果 if 判断条件 else 为假时的结果（注意，没有冒号）

a = 1
b = 2
func = a - b if a > b else a + b

print(func)
