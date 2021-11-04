# -*- coding: utf-8 -*-
# @Time :2021/8/1 12:00
# @Author : liufei
# @File :描述器.PY
"""
一个描述器类，一个描述器类的所有者。
当对描述器属性进行相关操作时，会触发描述器类中定义的方法。
当我们对描述器类所有类中的描述器属性访问修改操作时，会触发我们定义的描述器中的协议方法。
"""
class One(object):
    def __get__(self, instance, owner):
        print('访问属性，get方法被触发')
        print(instance)  # 描述器类所有者的对象
        print(owner)  # 描述器所有者类的类名
        return self.value


    def __set__(self, instance, value):
        print('修改属性，set方法被触发')
        print(self)  # 描述器对象
        print(instance)  # 对象实例
        print(value)  # 属性值
        self.value = value

    def __delete__(self, instance):
        print('删除属性，delete方法被触发')
        # del self.value
        self.value = None

class Two(object):
    name = 'liufei'
    attr = One()  # 描述器对象，
    # 当我们对这个属性进行操作时，会触发（描述器）One类中的方法，会覆盖原来类属性的相关操作（getattr、setattr等）。

t = Two()
t.attr = 10  #触发描述器中的set方法
del t.attr  #触发描述器中的delete方法
print(t.attr)  # 触发描述器中的get方法

