import logging
import unittest

import requests

from api.approve_api import ApproveApi
from api.login_api import LoginApi
from tools.assert_all import AssertAll


class TestApprove(unittest.TestCase):
    realname = "张德帅"
    card_id = "543222345678909876"

    def setUp(self) -> None:
        self.login = LoginApi()
        self.approve = ApproveApi()
        self.session = requests.session()
        self.assert_all = AssertAll()

    def tearDown(self) -> None:
        self.session.close()

    # 认证成功
    def test01_approve_success(self):
        # 前提要登录
        res = self.login.get_login(self.session)
        logging.info("登录成功{}".format(res.json()))
        self.assert_all.assert_all(res, "登录成功")
        response = self.approve.approve(self.session, self.realname, self.card_id)
        logging.info("认证成功{}".format(response.json()))
        print(response.json())
        self.assert_all.assert_all(response, "提交成功!")

    # # 已认证过,认证失败
    # def test02_approve_failed(self):
    #     # 前提要登录
    #     res = self.login.get_login(self.session)
    #     logging.info("登录成功{}".format(res.json()))
    #     self.assert_all.assert_all(res, "登录成功")
    #     response = self.approve.approve(self.session, "", self.card_id)
    #     logging.info("认证成功{}".format(response.json()))
    #     print(response.json())
    #     self.assert_all.assert_all(response, "认证失败!", 200, 100)
    #
    # # 身份证为空,认证失败
    # def test03_approve_failed(self):
    #     # 前提要登录
    #     res = self.login.get_login(self.session)
    #     logging.info("登录成功{}".format(res.json()))
    #     self.assert_all.assert_all(res, "登录成功")
    #     response = self.approve.approve(self.session, self.realname, "")
    #     logging.info("认证成功{}".format(response.json()))
    #     print(response.json())
    #     self.assert_all.assert_all(response, "身份证不能为空!", 200, 100, )

    # 获取认证信息
    def test04_get_approve(self):
        # 前提要登录
        res = self.login.get_login(self.session)
        logging.info("登录成功{}".format(res.json()))
        self.assert_all.assert_all(res, "登录成功")
        response = self.approve.get_approve(self.session)
        logging.info("获取认证信息{}".format(response.json()))
        print(response.json())
        self.assert_all.status_code(response)
        self.assertEqual("1", response.json().get("realname_card"))
