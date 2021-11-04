# -*- coding: utf-8 -*-
# @Time :2021/7/28 10:33
# @Author : liufei
# @File :多态.PY

class Base(object):
    def run(self):
        print("---base---run方法")


class Cat(Base):
    def run(self):
        print("---Cat---run方法")


class Dog(Base):
    def run(self):
        print("---Dog---run方法")

class Pig(object):
    def run(self):
        print("---非Base子类---run方法---")
"""这种行为称为多态。也就是说，方法调用将作用在 obj 的实际类型上。c_obj 是Base类型，
它实际上拥有自己的 run方法以及从 Base继承的 run方法，
但调用c_obj.run()总是先查找它自身的定义，如果没有定义，则顺着继承链向上查找，直到在某个父类中找到为止。"""

if __name__ == '__main__':
    b_obj = Base()
    c_obj = Cat()
    d_obj = Dog()
    p_obj = Pig()

    def func(obj):  # 由于Python是动态语言，所以，传递给函数 func(obj)的参数 obj 不一定是 Base 或 Base 的子类型。
        # 任何数据类型的实例都可以，只要它有一个run()的方法即可：
        obj.run()


    func(c_obj)
    func(p_obj)
