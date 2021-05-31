import app

# 认证
class ApproveApi:
    def __init__(self):
        self.approve_url = app.BASE_URL + "/member/realname/approverealname"
        self.get_approve_url = app.BASE_URL + "/member/member/getapprove"

    # 认证
    def approve(self, session, realname, card_id):
        data = {"realname": realname, "card_id": card_id}
        return session.post(self.approve_url, data=data, files={"": ""})

    # 查询认证信息
    def get_approve(self, session):
        return session.post(self.get_approve_url)
