# -*- coding: utf-8 -*-
# @Time :2021/7/31 11:44
# @Author : liufei
# @File :__dict__.PY

class CLanguage():
    a = 1
    b = 2
    def __init__ (self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"
    @classmethod
    def one(cls):
        print("rqfasdf")
# 通过类名调用__dict__
print(CLanguage.__dict__)
"""{'__module__': '__main__', 'a': 1, 'b': 2, '__init__': <function CLanguage.__init__ at 0x00000293ABC5CDC0>,
 'one': <classmethod object at 0x00000293ABB08400>, '__dict__': <attribute '__dict__' of 'CLanguage' objects>,
 '__weakref__': <attribute '__weakref__' of 'CLanguage' objects>, '__doc__': None}"""

# 通过类实例对象调用 __dict__
clangs = CLanguage()
print(clangs.__dict__)
"""{'name': 'C语言中文网', 'add': 'http://c.biancheng.net'}"""

# 对于具有继承关系的父类和子类来说，父类有自己的 __dict__，同样子类也有自己的 __dict__，它不会包含父类的 __dict__
class CLanguage():
    a = 1
    b = 2

    def __init__(self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"


class CL(CLanguage):
    c = 1
    d = 2

    def __init__(self):
        self.na = "Python教程"
        self.ad = "http://c.biancheng.net/python"


# 父类名调用__dict__
print(CLanguage.__dict__)
"""{'__module__': '__main__', 'a': 1, 'b': 2, '__init__': <function CLanguage.__init__ at 0x0000021DEBA6CDC0>, 
'__dict__': <attribute '__dict__' of 'CLanguage' objects>,
 '__weakref__': <attribute '__weakref__' of 'CLanguage' objects>, '__doc__': None}"""
# 子类名调用__dict__
print(CL.__dict__)
"""{'__module__': '__main__', 'c': 1, 'd': 2, '__init__': <function CL.__init__ at 0x0000021DEBA6D280>, '__doc__': None}"""

# 父类实例对象调用 __dict__
clangs = CLanguage()
print(clangs.__dict__)
"""{'name': 'C语言中文网', 'add': 'http://c.biancheng.net'}"""
# 子类实例对象调用 __dict__
cl = CL()
print(cl.__dict__)
"""{'na': 'Python教程', 'ad': 'http://c.biancheng.net/python'}"""