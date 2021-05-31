import logging

import pymysql

import app


class DBUtils:
    @classmethod
    def conn_database(cls, db_name):
        # autocommit自动提交
        return pymysql.Connect(host=app.BASE_DB_URL, port=app.BASE_DB_PORT, user=app.BASE_DB_USER,
                               password=app.BASE_DB_PWD, autocommit=True, database=db_name, charset="utf8")

    @classmethod
    def colse(cls, cursor=None, conn=None):
        if cursor:
            cursor.close()
        if conn:
            conn.cose()

    @classmethod
    # 数据清理
    def delete(cls, db_name, sql):
        conn = None
        try:
            conn = cls.conn_database(db_name)
            cursor = conn.cursor()
            cursor.execute(sql)
            # cursor.rowcount响应行数
            if 1 == cursor.rowcount:
                # 删除成功打印日志
                logging.info("delete sql success:{}".format(sql))
        # 如果出错回滚事务
        except Exception as e:
            conn.rollback()
        finally:
            cls.colse()
