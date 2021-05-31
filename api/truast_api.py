import app

# 充值
class TrustApi:
    def __init__(self):
        self.trust_url = app.BASE_URL + "/trust/trust/register"
        self.get_recharge_verify_code_url = app.BASE_URL + "/common/public/verifycode/"
        self.recharge_url = app.BASE_URL + "/trust/trust/recharge"

    def trust_register(self, session):
        return session.post(self.trust_url)

    def recharge_verify_code(self, session, r):
        url = self.get_recharge_verify_code_url + r
        return session.get(url)

    def recharge(self, session, paymentType="chinapnrTrust", formStr="reForm", amount="10000000", valicode="8888"):
        data = {"paymentType": paymentType, "amount": amount, "formStr": formStr, "valicode": valicode}
        return session.post(self.recharge_url, data=data)
