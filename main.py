import os
import time
import smtplib
import unittest
import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from cases.demo1.baidu import Baidu
from cases.demo2.spider_pics import SpiderPics
from cases.demo3.spider_fiction import SpiderFiction

class AllRun(unittest.TestCase):
    def setUp(self):
        self.bd = Baidu()
        self.sp = SpiderPics()
        self.sf = SpiderFiction()

    def test_baidu(self):
        u'''新浪账号登录百度并发帖子'''
        self.bd.main()

    @unittest.skip('skip')
    def test_spider_pics(self):
        u'''爬取图片存储到指定文件中'''
        self.sp.main()

    @unittest.skip('skip')
    def test_spider_fiction(self):
        u'''爬取小说内容并保存下来'''
        self.sf.step1()
        self.sf.step2()
        #self.sf.main()

    def tearDown(self):
        pass

if __name__ == "__main__":
    report = os.path.join(os.getcwd(), 'reports')
    casedir = os.path.join(os.getcwd(), 'cases', 'demo1')
    now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    filename = report+ '\\' + now + 'result.html' #定义个报告存放路径，支持相对路径。
    suite = unittest.TestSuite()
    #loadTestsFromTestCase()，传入TestCase
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(AllRun))

    with open(filename, 'wb+') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='SeleniumReport', description="This is seleniium demo!")
        runner.run(suite)