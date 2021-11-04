# -*- coding: utf-8 -*-
# @Time :2021/7/13 10:34
# @Author : liufei
# @File :flask-web.PY
from flask import Flask

# from settings import DevelopmentConfig
# from settings import ProductionConfig
# 创建flask类的对象 需要设置一个参数import_name :设置的时flask对象app所在的模块名
app = Flask(__name__)
# 查看应用的配置信息
print(app.config)


# app.config['ENV'] = 'development'#设置当前环境为开发环境
# app.config['DEBUG'] = True
# 从配置文件中加载配置信息
# app.config.from_object(DevelopmentConfig)

# 设置一个根路由
@app.route('/')
def index():
    return 'Hello Flask!'


# 路由
@app.route('/user')
def user_info():
    user_dict = {
        'name': '橙子',
        'age': 20,
        'sex': '女'
    }
    return user_dict


# 路由变量
# URL定位资源的路径中 有一个数据是变化的 每次变化对应着一组数据
@app.route('/phone/<brand>')
def phone(brand):  # 在路由中有变量的话 一定要在路由中绑定对应的变量
    '''
    在url中传递不同的变量值 需要再对应的视图函数中根据这个变量的数据 进行查询操作
    '''
    return '手机品牌' + brand


# 分页的情况 变量设置为页码
@app.route('/page/<int:page>')
def page_data(page):
    return f'正在请求第{page}页数据'


# 路由中变量必须加中尖括号 不加尖括号就是一个确定字段

# 路由中 路径后加不加/ 路由重定向
'''
加/ ==文件夹
不加 ==文件
加上/ 这个url路径 就相当于 访问文件夹 cd 切换文件夹的时候 后面加不加路径分隔符 都可以
访问资源的时候 后面加不加/ 都能请求定位嗷资源
'''


@app.route('/hello/')
def hello():
    return 'hello'


'''
类似于打开文件 直接写文件名 就能打开文件 但是在文件后面加路由路径分隔符 就找不到这个东西
请求资源的时候 不加可以请求资源 加上 就没有对应的资源啦
'''


@app.route('/nice')
def nice():
    return 'nice'


if __name__ == '__main__':
    # 启动flask对象 将其部署到服务器上
    # 可以指定访问服务器的地址 默认是127.0.0.1 只能当前计算机可以访问服务器把他设置成功
    # 可以指定访问服务器的端口号 默认是5000
    # debug 默认是false 在开发环境中建议开启跳水模式 应为开发阶段会经常修改代码 如果是非调试
    # 项目才可以访问新内容
    app.run()
