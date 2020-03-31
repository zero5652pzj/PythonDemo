from configparser import ConfigParser
from functools import lru_cache

class ReadIni:
    def __init__(self, file_path):
        self.file = file_path
        self.cf = self.connect()

    @lru_cache
    def connect(self):
        cf = ConfigParser()
        cf.read(self.file, encoding="utf-8")
        return cf

    # def options(self, sec):
    #     return self.cf.options(sec)

    def read_ini(self, sec, opt):
        value = self.cf.get(sec, opt)
        return value

def save(file, text):
    with open(file, 'w') as f:
        f.write(text)

import pymysql
from contextlib import contextmanager
@contextmanager
def connect_mysql(hostname, username, password, database, port=3306, charset='utf8'):
    conn = pymysql.connect(host=hostname, user=username, passwd=password, db=database, port=port, charset=charset)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        yield cursor
    finally:
        conn.commit()
        cursor.close()
        conn.close()


def beautiful_report(suite):
    import os
    import time
    from BeautifulReport import BeautifulReport
    report = os.path.join(os.getcwd(), 'reports')
    now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    filename = now + '_result.html' 
    result = BeautifulReport(suite)
    result.report(description='SeleniumReport', filename= filename, log_path=report)