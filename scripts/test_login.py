import logging
import random
import time

import allure
import pytest
import requests

from api.login_api import LoginApi
from tools.assert_all import AssertAll
from tools.json_util import json_util


# @allure.feature("注册登录模块")
# class TestLogin:
class TestLogin:
    # phone = "13490479087"
    # phone2 = "13433333333"
    # password = "a123456"

    def setup(self) -> None:
        self.login = LoginApi()
        self.assert_all = AssertAll()
        self.session = requests.session()

    def teardown(self) -> None:
        self.session.close()

    # @parameterized.expand(json_util("img_verify_code.json", "test_get_img_verify_code", "desc,type,status_code"))
    @pytest.mark.parametrize("args",
                             json_util("img_verify_code.json", "test1_get_img_verify_code", "desc,type,status_code"))
    @allure.story("测试验证码图片验证码")
    def test01_get_img_verify_code(self, args):
        print(args)
        allure.step(args[0])
        logging.info("测试验证码,{}".format(args[0]))
        # 随机小数
        # r = str(random.random())
        response = self.login.get_img_verify_code(self.session, str(random.random()))
        logging.info("测试验证码{}".format(response))
        print(response)
        self.assert_all.status_code(response)

    # 获取短信验证码成功
    @pytest.mark.parametrize("args",
                             json_util("sendsms_code.json", "test2_sendSms",
                                       "desc,imgVerifyCode,phone,status_code,status,description"))
    @allure.story("测试短信验证码")
    def test02_sendSms(self, args):
        self.login.get_img_verify_code(self.session, str(random.random()))
        allure.story(args[0])
        print(args[2])
        response = self.login.get_sendSms(self.session, imgVerifyCode=args[1], phone=args[2])
        logging.info("测试短信验证码{}".format(response.json()))
        print(response)
        self.assert_all.assert_all(response, args[5], args[3], args[4])

    # 注册成功
    @pytest.mark.parametrize("args",
                             json_util("register.json", "test03_register",
                                       "desc,imgVerifyCode,phone,password,dy_server,phone_code,"
                                       "status_code,status,description"))
    @allure.story("测试注册功能")
    def test03_register(self, args):
        allure.story(args[0])
        self.login.get_img_verify_code(self.session, str(random.random()))
        self.login.get_sendSms(self.session, imgVerifyCode=args[1], phone=args[2])
        response = self.login.get_register(self.session, phone=args[2], password=args[3], phone_code=args[5],
                                           dy_server=args[4], imgVerifyCode=args[1])
        logging.info("测试注册{}".format(response.json().get("description")))
        print(response.json())
        self.assert_all.assert_all(response, description=args[8], status_code=args[6], status=args[7])

    # 登录成功
    @pytest.mark.parametrize("args",
                             json_util("login.json", "test04_login",
                                       "desc,phone,password,status_code,status,description"))
    @allure.story("登录功能")
    def test04_login(self,args):
        allure.story(args[0])
        response = self.login.get_login(self.session, args[1], args[2])
        logging.info("测试登录{}".format(response.json().get("description")))
        self.assert_all.assert_all(response,description=args[5],status_code=args[3],status=args[4])
        i = 0
        if i <= 2:
            for i in range(2):
                i += 1
                response = self.login.get_login(self.session, args[1], args[2])
                logging.info("测试登录{}".format(response.json().get("description")))
                self.assert_all.assert_all(response, "密码错误{}次,达到3次将锁定账户".format(i), 200, 100, )
        if i == 2:
            response = self.login.get_login(self.session, args[1], args[2])
            logging.info("测试登录{}".format(response.json().get("description")))
            self.assert_all.assert_all(response, "由于连续输入错误密码达到上限，账号已被锁定，请于1.0分钟后重新登录", 200, 100)
        if i == 3:
            response = self.login.get_login(self.session, args[1], args[2])
            logging.info("测试登录{}".format(response.json().get("description")))
            self.assert_all.assert_all(response, "由于连续输入错误密码达到上限，账号已被锁定，请于1.0分钟后重新登录", 200, 100)
        else:
            time.sleep(61)
            response = self.login.get_login(self.session, args[1], args[2])
            logging.info("测试登录{}".format(response.json().get("description")))
        self.assert_all.assert_all(response, "登录成功")
