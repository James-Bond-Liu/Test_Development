# -*- coding: utf-8 -*-
# @Time :2021/7/7 16:55
# @Author : liufei
# @File :推导式.PY

"""列表推导式，[]

列表推导式是python构建列表list的一种快捷方式，是指轻量级循环创建列表
1.列表推导式会遍历后面的可迭代对象,然后按照for前的表达式进行运算,生成最终的列表.

2.如果有if条件语句,for遍历后紧跟着进行条件判断，然后进行for循环之前的运算，生成最后的列表

3.如果有多个for循环,则最终的数据数量为多个for循环的笛卡尔积.

4.可以进行嵌套的列表推导,与嵌套for循环的原理相同.
"""
import random

"""创建一个列表"""
# 创建一个0-10的列表
a = [x for x in range(11)]  # 利用列表推导式
print(a)  # 输出[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 等价于
a = []
for x in range(10):
    a.append(x)
print(a)

"""在列表推导式循环过程中使用if条件"""
# 创建一个1-10之间偶数的列表
a = [x for x in range(11) if x % 2 == 0]  # 输出结果：[0, 2, 4, 6, 8, 10]
# 等价于
a = []
for x in range(11):
    if x % 2 == 0:
        a.append(x)

"""两个for循环,得出笛卡尔乘积"""
a = [(x, y) for x in range(3) for y in range(3)]
print(a)  # 输出结果：[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]"""
# 等价于
a = []
for x in range(3):
    for y in range(3):
        a.append((x, y))

number = [e for e in range(1, 3) for f in range(5, 15, 5)]
print(number)
# 等价于
number2 = []
for e in range(1, 3):
    for f in range(5, 15, 5):
        number2.append(e)
print(number2)

"""字典推导式，{}
{键表达式：值表达式 for 循环}
"""

# 因为key是唯一的,所以最后value都是1
dict_a = {key: value for key in 'python' for value in range(2)}
print(dict_a)
"""{'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}"""
#等价于
a={}
for key in 'python':
    for value in range(2):
        a[key] = value

# 可以根据键来构造值
dict_b = {key: key * key for key in range(6)}
print(dict_b)
"""{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}"""

# 遍历一个有键值关系的可迭代对象
list_phone = [('HUAWEI', '华为'), ('MI', '小米'), ('OPPO', 'OPPO'), ('VIVO', 'VIVO')]
dict_c = {key: value for key, value in list_phone}
print(dict_c)
"""{'HUAWEI': '华为', 'MI': '小米', 'OPPO': 'OPPO', 'VIVO': 'VIVO'}"""

name = ["张三", "李四", "王五", "李六"]  # 保存名字列表
sign = ["白羊座", "双鱼座", "狮子座", "处女座"]  # 保存星座列表
dict1 = {i: j for i, j in zip(name, sign)}  # 字典推导式
print(dict1)  # {'张三': '白羊座', '李四': '双鱼座', '王五': '狮子座', '李六': '处女座'}

# 生成一个包含4个随机数的字典
random_dict = {i: random.randint(10, 100) for i in range(1, 5)}
print(random_dict)


"""生成器表达式，（）

生成器，保留生成器的计算规则，随用随取
用来节约内存，提高性能
返回一个生成器对象。
"""

exmple=(i for i in range(10))
print(exmple)

"""HomeWork"""
# 将如下字符串利用字典推导式生成字典
str_one = 'a=dkjfa;b=dfdj;c=dfjks;d=jfaeuiu;e=bhakj'
dict_d = {item.split('=')[0]:item.split('=')[1] for item in str_one.split(';')}



