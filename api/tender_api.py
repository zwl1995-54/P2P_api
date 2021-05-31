import app


# 投资
class TenderApi:
    def __init__(self, session):
        self.tender_id_url = app.BASE_URL + "/loan/loan/listtender"
        self.tender_info_url = app.BASE_URL + "/common/loan/loaninfo/"
        self.tender_url = app.BASE_URL + "/trust/trust/tender"
        self.tender_list_url = app.BASE_URL + "/loan/tender/mytenderlist"
        self.session = session

    # isTenderWord:yes判断投资是否加密(yes加密,no不加密)
    # "id":"2007"投资的id
    # "status_name": "借款中"
    # "name":13433333333借款有密码;;贷款标题
    # "name":13433333333借款无密码;;贷款标题
    # 投资密码:a123456
    # POST
    # http://user-p2p-test.itheima.net/loan/loan/listtender
    #
    # 获取投资产品id
    # id = 2007
    def get_tender_id(self, session, page="1"):
        data = {"page": page}
        return session.post(self.tender_id_url, data=data)

    # 获取投资产品详情
    # id = 2007
    def get_tender_info(self, session, id="1"):
        data = {"id": id}
        return session.post(self.tender_info_url, data=id)

    # 投资无密码
    def tender(self, id="1", amount="100", depositCertificate="-1"):
        data = {"id": id, "depositCertificate": depositCertificate, "amount": amount}
        return self.session.post(self.tender_list_url, data=data)

    # 投资有密码
    # id = 2046 & depositCertificate = -1 & amount = 1000 & password = a123456
    def tender_pwd(self, id="1", amount="100", depositCertificate="-1", password="a123456"):
        data = {"id": id, "depositCertificate": depositCertificate, "amount": amount, "password": password}
        return self.session.post(self.tender_url, data=data)

    # 查看投资列表
    def get_tender_list(self, status="tender", page="1"):
        data = {"status": status, "page": page}
        return self.session.post(self.tender_list_url, data=data)
