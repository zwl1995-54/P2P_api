import logging
import random
import unittest

import requests

from api.login_api import LoginApi
from api.truast_api import TrustApi
from tools.assert_all import AssertAll
from tools.third_request import ThirdRequest


# class TestTrust(unittest.TestCase):
class TestTrust:
    def setup(self) -> None:
        self.login = LoginApi()
        self.trust = TrustApi()
        self.third_request = ThirdRequest()
        self.assert_all = AssertAll()
        self.session = requests.session()

    def teardown(self) -> None:
        self.session.close()

    # 申请开户成功
    def test01_trust_success(self):
        # 前提要登录
        res = self.login.get_login(self.session)
        logging.info("登录成功{}".format(res.json()))
        self.assert_all.assert_all(res, "登录成功")
        response = self.trust.trust_register(self.session)
        logging.info("申请开户{}".format(response.json()))
        print(response.json())
        # 判断开户成功
        # assert_status_utils(self, response, 200)
        self.assert_all.status_code(response)
        # 获取字典form
        form_data = response.json().get("description").get("form")
        logging.info("开户记录{}".format(form_data))
        # 调用第三方接口开户
        res = self.third_request.get_third_request(form_data)
        # 断言
        self.assert_all.statuscode_text(res, "UserRegister OK")

    # 充值金额
    def test02_recharge_success(self):
        # 前提要登录
        res = self.login.get_login(self.session)
        logging.info("登录成功{}".format(res.json()))
        self.assert_all.assert_all(res, "登录成功")
        # 发送充值验证码
        code = self.trust.recharge_verify_code(self.session, str(random.random()))
        # 断言
        self.assert_all.status_code(code)
        # 发送充值请求
        response = self.trust.recharge(self.session)
        self.assert_all.statuscode_status(response)
        # 发送第三方请求
        # 获取响应中form表单
        form_data = response.json().get("description").get("form")
        logging.info("开户记录{}".format(form_data))
        # 调用第三方接口开户
        res = self.third_request.get_third_request(form_data)
        self.assert_all.statuscode_text(res, "NetSave OK")
