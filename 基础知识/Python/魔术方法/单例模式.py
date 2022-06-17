# -*- coding: utf-8 -*-
# @Time :2021/7/25 13:14
# @Author : liufei
# @File :单例模式.PY

class MyTest(object):
    instance = None

    def __new__(cls, *args, **kwargs):  # cls代表类本身即MyTest
        if not cls.instance:  # not和if判断语句组合使用，只有当not后面的语句为False时，冒号后面的语句体才会执行
            cls.instance = object.__new__(cls)  # 调用父类方法创建实例
            return cls.instance  # 调用类属性
        else:
            return cls.instance


t1 = MyTest()  # 无论创建几个实例，返回的都是第一个实例对象
t2 = MyTest()
t3 = MyTest()
print(id(t1))  # id()函数返回对象的唯一标识，可以理解为内存地址。
print(id(t2))
print(id(t3))
t1.name = 'panda'
print(t2.name)


# 装饰器实现单例模式，只要任意一个类使用该装饰器装饰，那么这个类就变成单例模式的类

def single(func):
    instance = {}

    def fun(*args, **kwargs):
        if func in instance:
            return instance[func]
        else:
            instance[func] = func(*args, **kwargs)
            return instance[func]
    return fun

@single  # 相当于 One = single(One)
class One():
    pass
