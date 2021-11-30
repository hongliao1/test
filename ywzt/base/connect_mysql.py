import logging
import MySQLdb
import pymysql

from sshtunnel import SSHTunnelForwarder
from ywzt.config import config


def connect_dev_mysql():
    db = MySQLdb.Connect(host='192.168.120.171', user='root', passwd='Rantion@test.321~', port=3306,
                         db='rantion_wms',
                         charset='utf8')
    # 创建游标
    cursor = db.cursor()
    # 执行sql语句
    cursor.execute('show tables')
    # 获取数据
    data = cursor.fetchall()
    print(data)


def connect_uat_mysql():
    server = SSHTunnelForwarder((config.ssh_ip, config.ssh_port),  # ssh的ip和端口号
                                ssh_password=config.ssh_passwd,  # ssh密码
                                ssh_username=config.ssh_user,  # ssh用户名
                                remote_bind_address=(config.uat_ip, config.uat_port))  # 数据库的ip和端口
    # 启动服务
    server.start()
    # print(server.local_bind_host)
    db = pymysql.Connect(host='127.0.0.1',  # 这里必须是’127.0.0.1‘
                         user=config.uat_user, passwd=config.uat_passwd,
                         port=server.local_bind_port,  # 端口号，用这个，不然报错
                         db=config.uat_db, charset='utf8')
    # 创建游标
    cursor = db.cursor()
    # 执行sql语句
    cursor.execute(config.sql)  # 获取数据
    data = cursor.fetchone()
    # print(data_1)
    db.close()
    server.close()
    return data[0]


class ConnectMySQL:
    def __init__(self, environment='uat'):
        if environment == 'dev':
            self.__str__()
            # print(type(self.connect_uat_mysql()))
        elif environment == 'uat':
            self.__str__()
            # print(type(self.__str__()))

    # 将地址转义成str
    def __str__(self):
        return '%s' % connect_uat_mysql()


def connect_mysql_1(num_1: int):
    def connect_mysql(func):
        def mysql(*args, **kwargs):
            # try:
            logging.basicConfig(level=logging.INFO)
            start = num()
            logging.info('初始数量：' + start)
            func(*args, **kwargs)
            end = num()
            logging.info('报损后的数量：' + end)
            assert int(start) - int(end) == num_1
            return func

        return mysql

    return connect_mysql


def num():
    num1 = ConnectMySQL().__str__()
    return num1


# 不可用于pytest，因为pytest不能存在__init__
class ConectMySQL_1:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        self.num_start = ConnectMySQL().__str__()
        logging.basicConfig(level=logging.INFO)
        logging.info('初始数量：' + self.num_start)
        self.func(self, *args, **kwargs)
        num_end = ConnectMySQL().__str__()
        logging.info('报损后的数量：' + num_end)
        # num = int(self.num_start) - int(num_end)
        print('初始数量：' + self.num_start)
