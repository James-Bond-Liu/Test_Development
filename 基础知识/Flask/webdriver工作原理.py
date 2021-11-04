# -*- coding: utf-8 -*-
# @Time    : 2021/10/8 19:35
# @Author  : Liu Fei
# @File    : webdriver工作原理.py
# @Software: PyCharm

import requests
from selenium import webdriver

# 直接利用webdriver驱动浏览器操作访问百度
driver = webdriver.Chrome(port=4567)  # 启动webdriver.exe服务。并且指定端口号运行这个服务。
driver.get('http://www.baidu.com')

#解析webdriver如何操作的浏览器访问网页
"""
启动webdiver服务
self.service = Service(
            executable_path,
            port=port,
            service_args=service_args,
            log_path=service_log_path)
        self.service.start()
        
链接客户端，创建一个链接到浏览器      
try:
    RemoteWebDriver.__init__(
        self,
        command_executor=ChromeRemoteConnection(
            remote_server_addr=self.service.service_url,
            keep_alive=keep_alive),
        desired_capabilities=desired_capabilities)
except Exception:
    self.quit()
    raise
    
driver.get相当于调用一个Command.GET接口，用post请求发起的。
Command.GET: ('POST', '/session/$sessionId/url'),

执行这个接口，并传入参数（url）
self.execute(Command.GET, {'url': url})
"""



# 通过启动webdriver服务，然后通过request接口发起请求webdriver中接口，操作浏览器访问百度】
data = {'url':'http://www.baidu.com'}
api_address = 'http://localhost:4567/session/{}/url'.format(driver.session_id)
res = requests.post(api_address, json=data)
print(res.status_code)
print(res)