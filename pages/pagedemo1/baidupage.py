from time import sleep
from cases.basepage import BasePage
from selenium.webdriver.support.wait import WebDriverWait

class Baidu(BasePage):
    def __init__(self):
        super().__init__()

    def get_ini_value(self, sec, opt):
        import os
        from utils.tools import ReadIni
        file = os.path.join(os.getcwd(),'data','baidu.ini')
        r = ReadIni(file)
        value = r.read_ini(sec, opt)
        return value

    def open_baidu_page(self, url):
        self.open(url)

    def search_setting(self, sec, opt, action):
        value = self.get_ini_value(sec, opt)
        above = self.link_text(value)
        self.action_chains(action, above)

    def search_key(self, value, *loc):
        el = self.find_element(*loc)
        self.send(el, value)

    def choose_cn(self, sec, opt1, opt2):
        css_locator = self.get_ini_value(sec, opt1)
        click = self.get_ini_value(sec, opt2)
        self.css(css_locator, click)
        sleep(2)

    def click_setting(self, locator, action):
        self.link_text(locator, action)

    def save_setting(self, sec, opt1, opt2):
        self.class_name(self.get_ini_value(sec, opt1), self.get_ini_value(sec, opt2))
        sleep(2)

    def click_login(self, locator, action):
        self.css(locator, action)
        self.wait(5)

    def click_weibo(self, locator, action):
        self.css(locator, action)
        self.wait(5)

    def change_weibo_handle(self, title):
        self.change_handle(title)
        self.wait(5)

    def input_account(self, locator_user, locator_pwd, method, sec, opt1, opt2):
        username = self.get_ini_value(sec, opt1)
        password = self.get_ini_value(sec, opt2)
        self.css(locator_user, method, username)
        self.wait(5)
        self.css(locator_pwd, method, password)
        sleep(2)

    def login_weibo(self, locator, method):
        self.css(locator, method)
        sleep(5)

    def click_tieba(self, title, method):
        WebDriverWait(self.drv,10,0.5).until(lambda drv:drv.find_element_by_link_text('贴吧'))
        self.link_text(title, method)
        self.wait(5)

    def search_python(self, locator, method, value):
        self.css(locator, method, value)
        self.wait(5)

    def enter_tieba(self, locator, method):
        self.link_text(locator, method)

    def click_tiezi(self, locator, method):
        self.css(locator, method)

    def input_text(self, locator, method, text):
        self.css(locator, method, text)
        sleep(2)

    def submit(self, locator, method):
        self.css(locator, method)
        self._refresh()
        sleep(2)
        self._close()

    def windowprompt(self):
        import pyautogui as pg
        value = pg.prompt("请输入您要编辑的内容：")
        return value

    def accept(self):
        self.alert_accept()

    def quit(self):
        self._quit()