# -*- coding: utf-8 -*-
# @Time :2021/7/6 9:49
# @Author : liufei
# @File :命名元组.PY
"""Python的元组不能为元组内部的数据进行命名，而 collections.namedtuple 可以来构造一个含有字段名称的元组类。

命名元组是一个类。
"""
from collections import namedtuple  # 利用此模块来创建一个命名元组类

# 定义一个命名元组类
User = namedtuple('User', ['name', 'age', 'id'])  # 第一个参数是命名元组类的类型名称，第二个参数命名元组类的属性。
                                                  # 返回对象和类型名称命名一般相同。
user = User('liu_fei', 26, 12306)  # 实例化命名元组类，括号内为实参。
print(user)
print( user.name, user.sex, user.age)  # 获取实例的属性，即通过命名元组元素名称获取元素具体值
print(user.name, user.id)  # 获取命名元组元素的方式

# 命名元组类的属性和方法
# 类属性 _fields：返回这个命名元组类的所有元素的名称
# 类方法 _make(iterable)：接受一个可迭代对象来生产这个命名元组类的实例
User._make(['zhangjing', 18, 110])
print(User._fields)  # name age id

"""
命名元组实例的方法
实例方法 _asdict()：把具名元组以 collections.OrdereDict 的形式返回，可以利用它来把元组里的信息友好的展示出来
实例方法_replace()：用于修改实例的属性
"""
# 使用 _replace() 修改实例对象属性
user = user._replace(age=22)

# 使用 _asdict()函数把 User对象转换成字典
print(user._asdict())  # {'name': 'liufei   ', 'year': 18, 'id': 110}


"""把字典或列表转换为命名元组"""
# 把字典转换为命名元组
dt={'name':'b', 'age':2, 'id':135}
ut=User(**dt)  # 输出User(name='b', age=2, id=135)

# 把列表转换为命名元组，使用map函数，调用命名元组类的_make函数，把列表转换为命名元组的列表
User = namedtuple('User', 'name age id')
list_users=map(User._make,[('u1',23,1001),('u2',21,1002),('u3',25,1003),])

# 把命名元组转换为列表, 列表中只有值，而没有字段名称
list(ut)  # 输出['b', '2', 135]

# 访问命名元组
# 通过逗号运算符和属性名来访问元组字段的值，例如，ut是命名元组的对象，name是对象的属性，可以通过以下方式访问元组的name属性：
ut.name
