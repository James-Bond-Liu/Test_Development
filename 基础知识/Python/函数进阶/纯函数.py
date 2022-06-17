# -*- coding: utf-8 -*-
# @Time :2021/7/10 15:18
# @Author : liufei
# @File :纯函数.PY

def func(n):
    print(n ** 2)


func(2)


# 内置函数(纯函数的一种)
# filter函数：传入两个参数位置1函数，位置2可迭代对象。对位置2可迭代对象进行遍历，然后传入位置1函数，通过函数的计算法则进行过滤，
# 返回一个filter对象。根据位置1函数是True还是False来决定是否将元素放到返回的对象中。
# filter(function, iterable) 相当于一个生成器表达式，当 function 不是 None 的时候为 (item for item in iterable if function(item))
def func(n):
    return n > 10


list1 = [1, 4, 5, 2, 56, 32, 76, 30]
res = filter(func, list1)
print(res)
print(tuple(res))


# map函数：
# 传入两个参数位置1函数，位置2可迭代对象。对位置2可迭代对象进行遍历，然后传入位置1函数，通过函数的计算将函数的返回值存储到返回map对象中.
# map(function, iterable) 相当于一个生成器表达式，当 function 不是 None 的时候为 (item for item in iterable if function(item))
def func2(n):
    return n * 2


list2 = [1, 3, 5, 6, 7, 99]
res2 = map(func2, list2)
print(res2)
print(list(res2))

# zip函数:接收多个可迭代的参数
# 将第一个参数的第一个元素和第二个参数的第一个元素取出来,打包成一个元组.同理后续相同操作.

res3 = zip([1, 3, 5], [2, 4, 6], ['a', 'b', 'c'], ['q', 'w', 'e'])
print(res3)
print(tuple(res3))
# 当可迭代的参数,长短不一时,会返回空None
res4 = zip([1, 3, 5], ['a', 'b', 'c', 'd', 'f'])
print(res3)
print(list(res3))
