# 1.导包
import unittest

import api
from api.api_login import ApiLogin
from parameterized import parameterized

from tools.get_log import GetLog
from tools.assesrt_common import assert_common
from tools.read_yaml import read_yaml
log = GetLog.get_logger()
# 2.新建测试类 继承unittest.TestCase
class Test01(unittest.TestCase):
    # 1.初始化
    def setUp(self):
        # 获取ApiLogin对象
        self.login = ApiLogin()

    # 2.登录测试接口方法
    @parameterized.expand(read_yaml("login.yaml"))
    def test_login(self,mobile,password):
        # 调用登录接口
        result = self.login.api_login(mobile,password)
        print("登录结果：",result.json())
        log.info("登录结果是：{}".format(result.json()))

        # 参数化json
        r = result.json()
        # 断言
        assert_common(self,result)
        # 提取token
        token = r.get("data")
        # 追加到公共变量
        api.headers["Authorization"] = "Bearer " + token
        print("追加token后的headers为：",api.headers)