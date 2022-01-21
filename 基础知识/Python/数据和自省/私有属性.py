# -*- coding: utf-8 -*-
# @Time :2021/7/31 11:28
# @Author : liufei
# @File :私有属性.PY

class Test():
    attr1 = 100  # 公有属性
    _attr2 = 200  # 私有属性（单下滑线开头）
    __attr3 = 300  # 私有属性（双下划线开头）


# 类属性可以通过类名和实例进行访问
# 访问公有属性
t = Test()
print(t.attr1)
print(Test.attr1)
# 访问单下滑线开头的私有属性
print(t._attr2)  # 通过t.attr2是访问不了属性的
print(Test._attr2)
# 访问双下划线开头的私有属性
# print(t.__attr3)  # 报错：'Test' object has no attribute '__attr3'
print(t._Test__attr3)  # 双下滑线开头的私有属性被python自动改名为“_类名__属性名”，所以在类外部访问时为_Test__attr3。
# 在类内部调用时不用加“_类名”
