'''
    该模块主要写的是关于selenium的基类，减少重复代码，方便调用
'''
import os
import time
import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class Base:
    def __init__(self):
        self.drv = self.driver()

    def driver(self):
        driver = webdriver.Chrome()
        return driver

    def id(self, params, mothod=None, value=None):
        '''
        mothod传入的值有:
        ['点击']:执行单击操作；
        ['输入']:针对输入框操作；
        '''
        if mothod == '点击':
            self.drv.find_element_by_id(params).click()
        elif mothod == '提交':
            self.drv.find_element_by_id(params).submit()
        elif mothod == '输入':
            self.drv.find_element_by_id(params).send_keys(value)
        elif mothod == None:
            element = self.drv.find_element_by_id(params)
            return element

    def name(self, params, mothod=None, value=None):
        '''
        mothod传入的值有:
        ['点击']:执行单击操作；
        ['输入']:针对输入框操作；
        '''
        if mothod == '点击':
            self.drv.find_element_by_name(params).click()
        elif mothod == '提交':
            self.drv.find_element_by_name(params).submit()
        elif mothod == '输入':
            self.drv.find_element_by_name(params).send_keys(value)
        elif mothod == None:
            element = self.drv.find_element_by_name(params)
            return element

    def css(self, params, mothod=None, value=None):
        '''
        mothod传入的值有:
        ['点击']:执行单击操作；
        ['输入']:针对输入框操作；
        '''
        if mothod == '点击':
            self.drv.find_element_by_css_selector(params).click()
        elif mothod == '提交':
            self.drv.find_element_by_css_selector(params).submit()
        elif mothod == '输入':
            self.drv.find_element_by_css_selector(params).send_keys(value)
        elif mothod == None:
            element = self.drv.find_element_by_css_selector(params)
            return element

    def class_name(self, params, mothod=None, value=None):
        '''
        mothod传入的值有:
        ['点击']:执行单击操作；
        ['输入']:针对输入框操作；
        '''
        if mothod == '点击':
            self.drv.find_element_by_class_name(params).click()
        elif mothod == '提交':
            self.drv.find_element_by_class_name(params).submit()
        elif mothod == '输入':
            self.drv.find_element_by_class_name(params).send_keys(value)
        elif mothod == None:
            element = self.drv.find_element_by_class_name(params)
            return element

    def link_text(self, params, mothod=None, value=None):
        '''
        mothod传入的值有:
        ['点击']:执行单击操作；
        ['输入']:针对输入框操作；
        '''
        if mothod == '点击':
            self.drv.find_element_by_link_text(params).click()
        elif mothod == '提交':
            self.drv.find_element_by_link_text(params).submit()
        elif mothod == '输入':
            self.drv.find_element_by_link_text(params).send_keys(value)
        elif mothod == None:
            element = self.drv.find_element_by_link_text(params)
            return element

    def max_window(self):
        self.drv.maximize_window()

    def min_window(self):
        self.drv.minimize_window()

    def action_chains(self, mothod, selector):
        if mothod == "悬停":
            ActionChains(self.drv).move_to_element(selector).perform()
        elif mothod == '右击':
            ActionChains(self.drv).context_click(selector).perform()

    def current_handle(self):
        '''
        当前页面的句柄
        '''
        return self.drv.current_window_handle

    def all_handles(self):
        '''
        获取打开页面所有句柄；
        如果句柄有所变动，需要重新获取；
        '''
        return self.drv.window_handles

    def change_handle(self, title):
        '''
        切换到想要的页面;
        page_title
        '''
        handles = self.all_handles()
        for handle in handles:
            want_handle = self.drv.switch_to.window(handle)
            page_title = self.drv.title
            if title in page_title:
                return want_handle
            continue

    def alert_prompt(self, text):
        value = pg.prompt(text)
        return value

    def alert_confirm(self, content, args):
        value = pg.confirm(content, buttons=args)
        return value

    def screenshot(self, filename):
        file = os.path.join(os.getcwd(),'pics', 'demo1') + "\\" + filename + ".png"
        self.drv.get_screenshot_as_file(file)

    def alert_accept(self):
        self.drv.switch_to.alert.accept()

    def alert_dismiss(self):
        self.drv.switch_to.alert.dismiss()

    def script(self, value):
        self.drv.execute_script(value)

    def refresh(self):
        self.drv.refresh()

    def wait(self, timeout):
        self.drv.implicitly_wait(timeout)

    def close(self):
        self.drv.close()

    def quit(self):
        self.drv.quit()