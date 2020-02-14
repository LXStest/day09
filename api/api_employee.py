import requests

import api
from tools.get_log import GetLog

log = GetLog.get_logger()
class ApiEployee:
    # 1.初始化
    def __init__(self):
    # 1.新增 url
        self.url1_post = api.host + "/api/sys/user"
    # 2.修改 ,查询,删除 url
        self.url1_num = api.host + "/api/sys/user/{}"

    # 2.新增员工
    def api_post_employee(self,username,mobile,workNumber):
        # 1.请求参数数据
        data = {"username":username,
                "mobile":mobile,
                "workNumber":workNumber}
        log.info("新增员工数据：{} 新增员工请求信息头：{}".format(data,api.headers))
        # 2.调用post方法 ->返回响应方法
        return requests.post(url=self.url1_post,json=data,headers=api.headers)
    # 3.修改员工
    def api_put_employee(self):
        # 1.参数数据
        data = {"username":"ton-gz-105"}
        log.info("修改后的数据：{}".format(data))
        # 2.调用put方法 ->返回响应方法
        return requests.put(url=self.url1_num.format(api.user_id),json=data,headers=api.headers)

    # 4.查询
    def api_get_employee(self):
        # 调用get方法 ->返回响应方法  注意:当前headers中存在content-Type不影响使用
        return requests.get(url=self.url1_num.format(api.user_id),headers=api.headers)

    # 5.删除员工
    def api_delete_employee(self):
        # 调用delete方法 ->返回响应方法
        return requests.delete(url=self.url1_num.format(api.user_id),headers=api.headers)