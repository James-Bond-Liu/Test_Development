# -*- coding: utf-8 -*-
# @Time :2021/7/9 9:33
# @Author : liufei
# @File :迭代器与生成器.PY

"""迭代器

迭代是Python最强大的功能之一，是访问集合元素的一种方式。
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter()和next()。
"""

# 字符串，列表或元组对象都可用于创建迭代器：
list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象
print(next(it))  # 输出迭代器的下一个元素，1
print(next(it))  # 2
for i in range(4):  #或者利用for循环输出
    print(next(it))

# 迭代器对象可以使用常规for语句进行遍历：
list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象
for x in it:
    print(x, end=" ")
# 输出：
# 1
# 2
# 3
# 4

# 也可以使用next()函数：
import sys  # 引入 sys 模块

list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
# 执行以上程序，输出结果如下：
#
# 1
# 2
# 3
# 4


创建一个迭代器
# 创建一个返回数字的迭代器，初始值为1，逐步递增
class MyNumbers:
    """把一个类作为一个迭代器使用需要在类中实现两个方法__iter__()与__next__() 。
    __iter__()方法返回一个特殊的迭代器对象，
    通过StopIteration异常标识迭代的完成。
    __next__()方法会返回下一个迭代器对象
    """
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print(next(myiter))
print(next(myiter))