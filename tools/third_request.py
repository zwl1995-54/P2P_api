import logging

import requests
from bs4 import BeautifulSoup



class ThirdRequest:

    def get_third_request(self, form_data):
        # 解析html
        soup = BeautifulSoup(form_data, "html.parser")
        # 获取标签名为form的属性为action的值
        url = soup.form["action"]
        print(url)
        data = {}
        # 遍历input标签
        for input in soup.find_all("input"):
            # 将input标签的name属性的值和value属性的值存到data字典中
            data.setdefault(input["name"], input["value"])
        logging.info("记录存到字典{}".format(data))
        # 给第三方发请求,并返回
        return requests.post(url, data=data)
        # assert_status_utils(self, res2, 200)
        # # print(res2.text)
        # # 断言是否成功
        # self.AssertAll("UserRegister OK", res2.text)
