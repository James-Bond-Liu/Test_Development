# -*- coding: utf-8 -*-
# @Time :2021/7/22 19:12
# @Author : liufei
# @File :多个装饰器装饰同一个函数.PY
import time

def deco1(func):
    print('这是第一个装饰器')
    def fun1(*args, **kwargs):
        print('--------start111--------')
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(end_time-start_time)
        print('---------end111----------')
    return fun1

def deco2(func):
    print('这是第二个装饰器')
    users = {'name':'panda', 'pwd':123, 'token':'False' }
    def fun2(*args, **kwargs):
        print('--------start222--------')
        if not users['token']==False:
            username = input('请输入账号：')
            password = int(input('请输入密码：'))
            if username == users['name'] and password == users['pwd']:
                users['token'] = True
                func(*args, **kwargs)
        else:
            func(*args, **kwargs)
        print('---------end222----------')
    return fun2

@deco2
@deco1
def demo():  # 多个装饰器装饰同一个函数：从下往上装饰，从上往下调用
    time.sleep(3)
    print('This is a demo')

demo()
