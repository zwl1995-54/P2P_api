import logging
import unittest

import requests
import yaml

from api.login_api import LoginApi
from api.tender_api import TenderApi
from tools.assert_all import AssertAll
from tools.connect_database import DBUtils
from tools.third_request import ThirdRequest


class TestTender(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
        self.login = LoginApi()
        self.third_request = ThirdRequest()
        self.assert_all = AssertAll()
        self.tender = TenderApi(self.session)

    def tearDown(self) -> None:
        self.session.close()
        logging.info("关闭session成功")
        # sql1 = "delete phone from mb_member_register_log where phone in('13490479087','1','1','1');"
        # DBUtils.delete(sql1)
        # logging.info("删除sql1{}成功".format(sql1))
        # sql2 = "delete i.* from mb_member_login_log i inner join mb_member m on i.member_id = m.id where m.phone in('13490479087','','','');"
        # DBUtils.delete(sql2)
        # logging.info("删除sql2{}成功".format(sql2))
        # sql3 = "delete i.* from mb_member_info i inner join mb_member m on i.member_id = m.id where m.phone in('13490479087','','','');"
        # DBUtils.delete(sql3)
        # logging.info("删除sql3{}成功".format(sql3))
        # sql4 = "delete i.* from mb_member where phone in('13490479087','','','');"
        # DBUtils.delete(sql4)
        # logging.info("删除sql4{}成功".format(sql4))

    # 投资
    def test01_tender(self):
        # 前提要登录
        res = self.login.get_login(self.session)
        logging.info("登录成功{}".format(res.json()))
        self.assert_all.assert_all(res, "登录成功")
        # 获取投资产品的id
        response = self.tender.get_tender_id(self.session)
        print(response.json())
        print(response.json().get("items")[0])
        logging.info("获取投资列表成功{}".format(response.json()))
        data = response.json().get("items")[0]
        print(type(data))
        data_list = []
        for key in data:
            print(key)
            if key == "id" or key == "isTenderWord" or key == "name":
                value = data[key]
            # isword = i.get("isTenderWord")
            # name = i.get("name")
                print(value)
                data_list.append(str(value))
        print(data_list[0], data_list)
        logging.info("获取投资产品id成功:{}".format(data_list[0]))
        # # 有密码
        # if data_list[1] == "yes" and data_list[2] == "13433333333有密码借款":
        #     # 获取投资产品详情
        #     response = self.tender.get_tender_info(self.session, id=str(data_list[0]))
        #     print(response.json())
        #     self.assert_all.statuscode_status(response)
        #     logging.info("获取投资产品详情成功{}".format(response.json()))
        # else:
        #     # 获取投资产品详情
        #     response = self.tender.get_tender_info(self.session, id=str(data_list[0]))
        #     self.assert_all.statuscode_status(response)
        #     logging.info("获取投资产品详情成功{}".format(response.json()))
        # 请求投资
        res1 = self.tender.tender_pwd(str(data_list[0]))
        # print(res1.text)
        self.assert_all.statuscode_status(res1)
        logging.info("投资成功{}".format(res1.json()))
        form_data = res1.json().get("description").get("form")
        res2 = self.third_request.get_third_request(form_data)
        self.assert_all.statuscode_text(res2, "InitiativeTender OK")
        logging.info("第三方投资成功{}".format(res2.text))
        # 获取我的投资列表
        res3 = self.tender.get_tender_list()
        print(res3.json())
        logging.info("获取我的投资列表成功:{}".format(res3.json()))
        self.assert_all.status_code(res3)
        # 查询列表的id
        my_id = res3.json().get("items")[0].get("loan_id")
        # 如果id=投资的id
        if my_id == data_list[0]:
            print("ok")
        logging.info("投资成功:{}".format(res3.json()))

    # def get_data(self, response,):
    #     data = response.json().get("items")[0]
    #     data_list = []
    #     for i in data:
    #         if i == "id" or i == "loanId" or i == "loan_id" and i == "loan_name" or i=="name":
    #             for j in range(1):
    #                 ele = i.get(str(i))
    #                 data_list.append(str(ele))
                # isword = i.get("isTenderWord")
                # name = i.get("name")
                # data_list.append(str(id, isword, name))

        # logging.info("申请开户{}".format(response.json()))
        # print(response.json())
        # # 判断开户成功
        # # assert_status_utils(self, response, 200)
        # self.assert_all.status_code(response)
        # # 获取字典form
        # form_data = response.json().get("description").get("form")
        # logging.info("开户记录{}".format(form_data))
        # # 调用第三方接口开户
        # res = self.third_request.get_third_request(form_data)
        # # 断言
