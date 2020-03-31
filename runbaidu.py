import unittest
from time import sleep
from pages.pagedemo1.baidupage import Baidu
from utils.tools import beautiful_report

class RunBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.b = Baidu()

    def test_open(self):
        '''打开百度页面'''
        self.b.open_baidu_page('http://www.baidu.com')
        self.b.wait(3)

    def test_search(self):
        '''设置悬停，并保存设置'''
        self.b.search_setting('step1', '我要设置', '悬停')
        self.b.wait(3)
        self.b.click_setting("搜索设置",'点击')
        sleep(2)
        self.b.choose_cn('step1', '简体中文', '点击')
        sleep(2)
        self.b.save_setting('step1', '保存设置', '点击')
        sleep(2)
        self.b.accept()

    def test_login(self):
        '''用微博账号登录百度'''
        self.b.click_login('#u1 > a.lb', '点击')
        self.b.click_weibo("#pass_phoenix_btn > ul > li.bd-acc-tsina > a", '点击')
        self.b.change_handle('网站链接')
        self.b.input_account(locator_user='#userId', locator_pwd='#passwd', method='输入', sec='account', opt1='username', opt2='password')
        self.b.login_weibo("#outer > div > div.WB_panel.oauth_main > form > div > div.oauth_login_box01.clearfix > div > p > a.WB_btn_login.formbtn_01", '提交')

    def test_enter_tieba(self):
        '''进入python贴吧'''
        self.b.change_handle('百度一下')
        self.b.click_tieba('贴吧', '点击')
        self.b.change_weibo_handle("百度贴吧")
        self.b.screenshot('百度贴吧')
        self.b.search_python('#wd1', '输入', 'python')
        self.b.enter_tieba('进入贴吧', '点击')

    def test_click_tiezi(self):
        '''进入置顶帖子，并评论'''
        self.b.click_tiezi('#thread_top_list > li:nth-child(1) > div > div.col2_right.j_threadlist_li_right > div > div.threadlist_title.pull_left.j_th_tit > a', '点击')
        self.b.change_weibo_handle('python吧吧友交流群')
        self.b.input_text('#ueditor_replace', '输入', self.b.windowprompt())
        self.b.submit("#tb_rich_poster > div.poster_body.editor_wrapper > div.poster_component.editor_bottom_panel.clearfix > div > a > span > em", '点击')

    @classmethod
    def tearDownClass(cls):
        sleep(2)
        cls.b.quit()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    tests = ['test_open', 'test_search', 'test_login', 'test_enter_tieba', 'test_click_tiezi']
    for test in tests:
        suite.addTest(RunBaidu(test))
    beautiful_report(suite)