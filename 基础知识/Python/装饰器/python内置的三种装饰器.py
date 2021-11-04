# -*- coding: utf-8 -*-
# @Time :2021/7/24 12:23
# @Author : liufei
# @File :python内置的三种装饰器.PY

class Teacher():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sex = 'M'
    def cooking(self, *args):  # 实例方法
        for k in args:
            print(self.name + "性别" + self.sex + "会做{0}".format(k))


    # 静态方法和类方法不可以调用类中属性的值，必须自己传递。
    @classmethod
    def swimming(cls):  # 类方法
        print("会游泳")

    @staticmethod
    def singing():  # 静态方法(普通函数)
        print("会给同学唱歌")

    @property
    def codeing(self):
        return 2

t = Teacher('panda', 38)  # 实例化对象
t.cooking()  # 实例调用实例方法
Teacher.swimming()  # 类直接调用类方法，不用先实例化类
Teacher.singing()  # 类直接调用静态方法，不用先实例化类
Teacher.codeing  # 类直接调用经过@property装饰的方法。将某函数，做为属性使用 ，且这个属性不可以更改。
