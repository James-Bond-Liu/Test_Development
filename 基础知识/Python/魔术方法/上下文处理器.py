# -*- coding: utf-8 -*-
# @Time :2021/7/27 18:42
# @Author : liufei
# @File :上下文处理器.PY

"""自定义一个上下文管理器，模拟with文件操作"""


class MyOpen(object):
    def __init__(self, path, mode):
        # 记录要操作的文件路径和模式
        self.path = path
        self.mode = mode

    def __enter__(self):
        print('代码执行到了__enter__......')
        # 打开文件
        # self.handle是一个实例变量，这样就扩大了变量的引用范围。类似于global全局变量的作用
        self.handle = open(self.path, self.mode)
        # 返回打开的文件对象引用, 用来给  as 后的变量f赋值
        return self.handle

    # 退出方法中，用来实现善后处理工作
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('代码执行到了__exit__......')
        self.handle.close()


# a+ 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
with MyOpen('test.txt', 'a+') as f:  # 上下文管理器即MyOpen()实例化的对象
    # 创建写入文件
    f.write("Hello Python!!!")
    print("文件写入成功")

"""编写两个数做除法的程序，然后给除数穿入"""


class MyCount(object):
    # 接收两个参数
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 返回一个地址（实质是被as后的变量接收），实例对象就会执行MyCount中的方法:div()
    def __enter__(self):
        print('代码执行到了__enter__......')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("代码执行到了__exit__......")
        if exc_type == None:
            print('程序没问题')
        else:
            print('程序有问题，如果你能你看懂，问题如下：')
            print('Type-异常类型: ', exc_type)
            print('Value-异常值:', exc_val)
            print('TreacBack-异常回源追踪:', exc_tb)

        # 返回值决定了捕获的异常是否继续向外抛出
        # 如果是 False 那么就会继续向外抛出，程序终端会看到系统提示的异常信息
        # 如果是 True 不会向外抛出，程序看不到系统提示信息，只能看到else中的输出
        # return False
        return True

    def div(self):
        print("代码执行到了除法div")
        return self.x / self.y


with MyCount(1, 0) as mc:  # 上下文管理器即MyOpen()实例化的对象，等同于mc = MyCount(1,0)
    print("********")
    mc.div()  # 调用类方法

# 创建一个数据库的上下文管理器
import pymysql


class DataBase():
    def __init__(self, data_conf):
        self.connect = pymysql.connect(**data_conf)
        self.cusor = self.connect.cursor()

    def __enter__(self):
        return self.cusor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cusor.close()
        self.connect.close()


database_conf = dict(
    host='localhost',
    user='root',
    password='mysql',
    database='test',
    port=3306,
    chartset='utf-8'
)

with DataBase(database_conf) as cur:
    cur.execute('select * from students')
    print(cur.fetchall())