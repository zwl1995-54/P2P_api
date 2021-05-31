# 初始化日志函数
import logging
import os
import time
from logging import handlers

import app


class GetLogger:
    logger = None

    @classmethod
    def get_logger(cls, fileName):
        # 如果logger为空
        if cls.logger is None:
            # 获取日志器
            cls.logger = logging.getLogger()
            # 设置日志器格式
            cls.logger.setLevel(logging.INFO)
            # 获取处理器
            sh = logging.StreamHandler()
            filename = app.BASE_PATH + "%slog%s%s" % (os.sep, os.sep, fileName+"{}.log".format(time.strftime("%Y%m%d-%H%M%S")))
            # 获取处理文件
            th = logging.handlers.TimedRotatingFileHandler(filename=filename,
                                                           when="M",
                                                           interval=10,
                                                           backupCount=30,
                                                           encoding="UTF-8")
            # 设置格式
            fmt = "%(asctime)s%(levelname)s[%(name)s][%(filename)s(%(funcName)s" \
                  ":%(lineno)d)-%(message)s]"
            # 格式化器
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器中
            sh.setFormatter(fm)
            th.setFormatter(fm)
            # 将处理器放到日志器中
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)

        # 返回日志器
        return cls.logger


def test():
    GetLogger.get_logger()
    logging.info("info")
    logging.error("error")
    logging.debug("debug")
