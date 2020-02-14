import unittest
import api
from api.api_employee import ApiEployee
from tools.get_log import GetLog

from tools.assesrt_common import assert_common
from parameterized import parameterized

from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestEmployee(unittest.TestCase):
    # 1.初始化方法
    @classmethod
    def setUpClass(cls):
        # 获取ApiEmployee对象
        cls.login = ApiEployee()

    # 2.新增员工 接口测试方法
    @parameterized.expand(read_yaml("employee_post.yaml"))
    def test01_post(self, username, mobile, workNumber):
        r = self.login.api_post_employee(username, mobile, workNumber)
        # 断言
        assert_common(self, r)
        print("新增员工结果:", r.json())
        log.info("新增员工结果：{}".format(r.json()))
        # 提取user_id
        api.user_id = r.json().get("data").get("id")
        print("员工user_id值为：", api.user_id)
        log.info("员工user_id值为：{}".format(api.user_id))

    # 3.更新员工 接口测试方法
    def test02_put(self):
        # 1.调用更新接口
        r = self.login.api_put_employee()
        # 2.断言
        assert_common(self, r)
        log.info("更新员工结果：{}".format(r.json()))

    # 4.查询员工 接口测试方法
    def test03_get(self):
        # 1.调用查询接口
        r = self.login.api_get_employee()
        # 2.断言
        assert_common(self, r)
        log.info("查询员工结果：{}".format(r.json()))

    # 5.删除员工 接口测试方法
    def test04_delete(self):
        r = self.login.api_delete_employee()
        print("删除结果为：", r.json())
        # 断言
        assert_common(self, r)
        log.info("删除员工结果：{}".format(r.json()))
