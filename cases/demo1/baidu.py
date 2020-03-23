import os
import time
import pyautogui as pg
from cases.base import Base
from utils.tools import ReadIni
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Baidu(Base):
    def __init__(self):
        super().__init__()
        file = os.path.join(os.getcwd(),'data','baidu.ini')
        self.r = ReadIni(file)

    def open_page(self):
        self.drv.get("http://www.baidu.com")

    def get_value(self, sec, opt):
        value = self.r.read_ini(sec, opt)
        return value

    def step1(self):
        '''
        进行设置操作，此界面需要用到悬浮和弹窗
        '''
        step1 = 'step1'
        #1. 打开百度首页
        self.open_page()
        #2.窗口最大化
        self.max_window()
        #3.悬浮到设置元素
        above = self.link_text(self.get_value(step1,'我要设置'))
        self.action_chains('悬停', above)
        #4.点击搜索设置
        self.link_text("搜索设置",'点击')
        time.sleep(2)
        #5.点击'仅简体中文'
        self.css(self.get_value(step1, '简体中文'), self.get_value(step1, '点击'))
        self.wait(5)
        #6.保存设置
        self.class_name(self.get_value(step1, '保存设置'), self.get_value(step1, '点击'))
        time.sleep(3)
        #7.弹窗确认
        self.alert_accept()

    def step2(self):
        '''
        使用微博登录百度账号
        '''
        #8.点击登录
        self.css('#u1 > a.lb', '点击')
        self.wait(5)
        #9.点击微博
        self.css("#pass_phoenix_btn > ul > li.bd-acc-tsina > a", '点击')
        self.wait(5)
        #10.切换微博登录页面
        self.change_handle('网站链接')
        self.wait(5)
        #11.#输入密码帐号
        self.css('#userId', '输入', self.get_value('account','username'))
        self.wait(5)
        self.css('#passwd','输入',self.get_value('account','password'))
        time.sleep(2)
        #12.微博登录
        self.css("#outer > div > div.WB_panel.oauth_main > form > div > div.oauth_login_box01.clearfix > div > p > a.WB_btn_login.formbtn_01", '提交')
        time.sleep(5)
        #13.切换到百度首页
        self.change_handle('百度一下')
        self.wait(5)
        #14.点击贴吧
        self.link_text('贴吧', '点击')
        self.wait(5)
        #15.切换到贴吧句柄
        self.change_handle("百度贴吧")
        self.screenshot('百度贴吧')

    def step3(self):
        '''
        进入贴吧，跟帖发表内容后退出
        '''
        #17.搜索python吧
        self.css('#wd1', '输入', 'python')
        self.screenshot('搜索python')
        self.wait(5)
        #18.进入贴吧
        self.link_text('进入贴吧', '点击')
        self.wait(5)
        #19.点击进入置顶帖子
        self.css('#thread_top_list > li:nth-child(1) > div > div.col2_right.j_threadlist_li_right > div > div.threadlist_title.pull_left.j_th_tit > a', '点击')
        #20.进入帖子句柄
        self.change_handle('python吧吧友交流群')
        time.sleep(2)
        #21.拉到最下面
        js = "window.scrollTo(100,20000)"
        self.script(js)
        #22.输入发表内容
        value = pg.prompt("请输入您要编辑的内容：")
        self.css('#ueditor_replace','输入', value)
        time.sleep(2)
        #23.点击发表
        self.css("#tb_rich_poster > div.poster_body.editor_wrapper > div.poster_component.editor_bottom_panel.clearfix > div > a > span > em", '点击')
        #24.关闭当前页面
        self.refresh()
        js = "window.scrollTo(100,20000)"
        self.script(js)
        self.close()


    def step4(self):
        #25.回到首页并刷新
        self.change_handle('百度一下')
        self.refresh()
        #26.鼠标移动到帐号名称上
        login_count = self.css("#s_username_top > span")
        self.action_chains('悬停', login_count)
        #27.点击退出账号
        self.link_text("退出", '点击')
        #28.弹窗确认
        self.link_text('确定', '点击')
        #29.页面刷新，确认退出
        self.refresh()
        #30.退出Chrome
        self.quit()

    def main(self):
        try:
            self.step1()
            self.step2()
            self.step3()
            self.step4()
        finally:
            self.quit()


if __name__ == "__main__":
    b = Baidu()
    b.main() 