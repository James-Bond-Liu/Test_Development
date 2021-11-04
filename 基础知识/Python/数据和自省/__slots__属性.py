# -*- coding: utf-8 -*-
# @Time :2021/7/31 12:24
# @Author : liufei
# @File :__slots__属性.PY

class Base():

    __slots__ = ['name', 'age']  # 限定类实例化对象所能绑定的属性
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #self.sex = 'man'  # 报错：AttributeError: 'Base' object has no attribute 'sex'
    def demo(self):
        print('{}岁的{}'.format(self.age, self.name))

b = Base('panda', 4)
# b.sex = 'women'  # 报错：AttributeError: 'Base' object has no attribute 'sex'
# 实例对象只能使用__slots__限定的属性

# print(b.__dict__) # 报错：AttributeError: 'Base' object has no attribute '__dict__'
# 由于在类定义中定义了__slots__属性，所以类实例则不会再默认创建__dict__属性
print(Base.__dict__)  # 类本身还是拥有__dict__属性的