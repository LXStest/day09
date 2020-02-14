"""
资源接口封装
"""
# 创建一个封装类
import requests
import api
from tools.get_log import GetLog

log = GetLog.get_logger()
class ApiLogin():
    # 1.初始化
    def __init__(self):
    #     组装登录url
        self.url_login = api.host + "/api/sys/login"
        log.info("正在初始化登录url：".format(self.url_login))

    # 登录接口封装
    def api_login(self,mobile,password):
    #     1.定义测试数据
        data = {"mobile":mobile,"password":password}
        log.info("正在初始化数据：{} 请求头信息：{} ".format(data,api.headers))
    #     2.调用post方法，注意：一定要将响应对象返回

        return requests.post(url=self.url_login,json=data,headers=api.headers)

