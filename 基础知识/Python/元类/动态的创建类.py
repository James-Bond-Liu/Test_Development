# -*- coding: utf-8 -*-
# @Time :2021/8/5 20:08
# @Author : liufei
# @File :动态的创建类.PY

# 1、构建Foo类
class Foo(object):
    bar = True


# 使用type构建（底层就是以type创建的类）
Foo = type('Foo', (), {'bar': True})


# 2.继承Foo类
class FooChild(Foo):
    pass


# 使用type构建
FooChild = type('FooChild', (Foo,), {})

print(FooChild)  # 输出：<class '__main__.FooChild'>
print(FooChild.bar)  # bar属性是由Foo继承而来，输出：True


# 3.为Foochild类增加方法
def echo_bar(self):
    print(self.bar)

FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})

hasattr(Foo, 'echo_bar')  # 输出：False

hasattr(FooChild, 'echo_bar')  # 输出：True

my_foo = FooChild()

my_foo.echo_bar()
# 输出：True
