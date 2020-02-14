from tools.get_log import GetLog

log = GetLog.get_logger()
def assert_common(self,response,
                  status_code=200,
                  success=True,
                  code=10000,
                  message="操作成功！"):
    # 参数化json
    # 日志
    try:
        r = response.json()
        # 1.断言状态码200
        self.assertEqual(status_code, response.status_code)
        # 2.断言success true
        self.assertEqual(success, r.get("success"))
        # 3.断言code 10000
        self.assertEqual(code, r.get("code"))
        # 4.断言msg
        self.assertEqual(message, r.get("message"))
    except Exception as e:
        log.error(e)

        # raise





