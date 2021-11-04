# -*- coding: utf-8 -*-
# @Time :2021/8/1 10:12
# @Author : liufei
# @File :自定义属性访问.PY

class Test():
    number = 10

    def __getattribute__(self, item):
        print('类对象访问属性的时候自动触发getattribute方法')
        print(item)
        return object.__getattribute__(self, item)  # 继承父类中的方法，维持原功能。

    def __getattr__(self, item):  # 访问属性时，先触发getattribute方法，找不到报错后，然后会触发此方法
        print('类对象访问属性，报错AttrError时，会自动触发getattr方法')
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):  # key=属性名，value=属性值
        print('类对象修改属性的时候自动触发setattr方法')
        print(key)
        print(value)
        return super().__setattr__(key, value)  # 继承父类方法，维持原有功能

    def __delattr__(self, item):
        print('类对象删除属性的时候自动触发delattr方法')
        print(item)
        super().__delattr__(item)


t = Test()
print(t.number)  # 触发getattr
print(t.name)  # 触发getattribute和getattr
t.number = 20  # 触发setattr
del t.number  # 触发delattr