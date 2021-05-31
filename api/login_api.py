import app

# 登录注册

class LoginApi:
    def __init__(self):
        self.verify_code_url = app.BASE_URL + "/common/public/verifycode/"
        self.sendSms_url = app.BASE_URL + "/member/public/sendSms"
        self.register_url = app.BASE_URL + "/member/public/reg"
        self.login_url = app.BASE_URL + "/member/public/login"

    def get_img_verify_code(self, session, random):
        url = self.verify_code_url + random
        return session.get(url)

    def get_sendSms(self, session, phone, imgVerifyCode="8888", type="reg"):
        data = {"phone": phone, "imgVerifyCode": imgVerifyCode, "type": type}
        url = self.sendSms_url
        return session.post(url, data=data)

    def get_register(self, session, phone, password, imgVerifyCode="8888", phone_code="666666", dy_server="on"):
        data = {"phone": phone, "password": password, "verifycode": imgVerifyCode, "phone_code": phone_code,
                "dy_server": dy_server}
        url = self.register_url
        return session.post(url, data=data)

    def get_login(self, session, phone="13490479087", password="a123456"):
        data = {"keywords": phone, "password": password}
        url = self.login_url
        return session.post(url, data=data)
