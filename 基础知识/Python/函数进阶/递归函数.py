# -*- coding: utf-8 -*-
# @Time :2021/7/10 15:11
# @Author : liufei
# @File :递归函数.PY

"""递归最大次数1000次"""

# 需求：通过递归函数实现任意数值的阶乘
def gen(n):
    if n == 1:  # 递归临界点
        return n
    else:
        return n * gen(n - 1)  # 不等于1则再次调用函数自身进行运算


res = gen(3)
print(res)

"""homework"""


# 实现斐波那契数列，输入一个数列的位置数，反回斐波那契数列相应位置的值。斐波那契数列[1，1，2，3，5，8，13，21，34，......]，第一个数是1，后面的数等于前两个数相加的结果
def func1(n):
    if (n == 1 or n == 2):
        return 1
    else:
        return func1(n - 1) + func1(n - 2)


# 经典问题：有一对兔子，第三个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？（意味着生长期为2）
"""
第一个月：1对---1
第二个月：1对---1
第三个月：1+1对---2
第四个月：2+1对---3
第五个月：3+2对---5
第六个月：5+3对---8
第七个月：8+5对---13
第八个月：13+8对---21
"""


def func2(n):
    if (n == 1 or n == 2):
        return 2
    else:
        return func1(n - 1) + func1(n - 2)


# 小明有100元钱，打算买100本书，A类书籍5元一本，B类书籍3元一本，C类书籍1元两本，请用程序算出小明一共有多少种买法？
money = 100
book = 100
count = 0
for a in range(money / 5):  # A类书籍可以买a本
    for b in range(money / 3):  # B类书籍可以买b本
        for c in range(money / 0.5):  # C类书籍可以买c本
            if a * 5 + b * 3 + c * 0.5 <= 100 and a + b + c == 100:
                print(a, b, c)
                count += 1
print("小明一共有{0}种买法".format(count))
