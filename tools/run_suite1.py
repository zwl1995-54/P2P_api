import os
import time
import unittest

import app

# from scripts.test01_login import TestLogin
# from scripts.test02_approve import TestApprove
# from scripts.test03_trust import TestTrust
# from scripts.test04_tender import TestTender
# from tools.HTMLTestRunner import HTMLTestRunner
#
# # 组织测试套件
# # 创建suite对象
# suite = unittest.TestSuite()
# # 添加要执行的函数
# suite.addTest(unittest.makeSuite(TestLogin))
# suite.addTest(unittest.makeSuite(TestApprove))
# suite.addTest(unittest.makeSuite(TestTrust))
# suite.addTest(unittest.makeSuite(TestTender))
# # 指定测试报告生成的路径
# path = app.BASE_PATH + "%sreport%s%s" % (os.sep, os.sep, format(time.strftime("%Y%m%d-%H%M%S")) + ".html")
# with open(path, "wb") as f:
#     # 创建HTMLTESTRunner运行器
#     runner = HTMLTestRunner(f, title="api report", description="test")
#     #     执行测试套件
#     runner.run(suite)
# case路径

case_path = app.BASE_PATH + "%sscripts%s" % (os.sep, os.sep)
# 指定测试报告生成的路径
report_path = app.BASE_PATH + "%sreport%s%s" % (os.sep, os.sep, format(time.strftime("%Y%m%d-%H%M%S")) + ".html")

# def all_case():
#     discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)
#     print(discover)
#     return discover
#
# if __name__ == '__main__':
#     from tools.HTMLTestRunner import HTMLTestRunner
# 
#     fp = open(report_path, "wb")
#     # with open(path, "wb") as f:
#     runner = HTMLTestRunner(fp, title="接口测试", description="test")
#     # runner = unittest.TextTestRunner(f,descriptions="test")
#     runner.run(all_case())
#     fp.close()
