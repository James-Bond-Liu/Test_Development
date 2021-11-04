# -*- coding: utf-8 -*-
# @Time    : 2021/9/20 11:51
# @Author  : Liu Fei
# @File    : model.py
# @Software: PyCharm

# 后台框架
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# 测试数据
user_info = {'user': 'python01', 'pwd': 'lemonban'}
project_data = {'code': '1', 'data': [{'title': '前程贷', 'id': '1001'}, {'title': '智慧金融', 'id': '1002'},
                                      {'title': '生鲜到家', 'id': '1003'}, {'title': '柠檬版app', 'id': '1004'}],
                'msg': '四个项目'}

# 接口数据
interface_data = {
    '1001': {'code': '1', 'data': [{'name': '登录1001'}, {'name': '注册1001'}], 'msg': '两个接口'},
    '1002': {'code': '1', 'data': [{'name': '登录1002'}, {'name': '注册1002'}, {'name': '贷款1002'}], 'msg': '三个接口'},
    '1003': {'code': '1', 'data': [{'name': '登录1003'}, {'name': '注册1003'}, {'name': '下单1003'}], 'msg': '三个接口'},
    '1004': {'code': '1', 'data': [{'name': '登录1004'}, {'name': '注册1004'}, {'name': '报名1004'}, {'name': '缴费1004'}],
             'msg': '四个接口'},
}


# 首页
@app.route('/', methods=['get'])
def index():
    return render_template(r'model.html')


# 登录
@app.route('/login', methods=['post'])
def login():
    data = request.form
    # 判断账号，密码是否正确
    if user_info.get('user') == data.get('user') and user_info.get('pwd') ==data.get('pwd'):
        return jsonify({'code': '1', 'data': None, 'msg': '成功'})
    else:
        return jsonify({'code': '0', 'data': None, 'msg': '账号或密码有误'})


# 查询项目列表
@app.route('/pro_list', methods=['get'])
def pro_list():
    return jsonify(project_data)


# 获取接口列表
@app.route('/interface', methods=['post'])
def interface():
    inter_id = request.form.get('pro_id')
    if inter_id:
        res_data = interface_data.get(inter_id)
        if res_data:
            return jsonify(res_data)
        else:
            return jsonify({'code': '0', 'data': None, 'msg': '没有这个项目'})
    else:
        return jsonify({'code': '0', 'data': None, 'msg': '请求参数不能为空'})


if __name__ == '__main__':
    app.run(debug=True)
