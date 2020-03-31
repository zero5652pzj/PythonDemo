from selenium import webdriver

class BasePage:
    def __init__(self, driver='Chrome'):
        self.drv = self.driver(driver)

    def driver(self, driver):
        if driver == 'Chrome':
            drv = webdriver.Chrome()
        elif driver == 'Firefox':
            drv = webdriver.Firefox()
        elif driver == 'Edge':
            drv = webdriver.Edge()
        return drv

    def open(self, url):
        self.drv.get(url)
        self.drv.maximize_window()

    def find_element(self, *loc):
        element = self.drv.find_element(*loc)
        return element

    def send(self, el, value):
        el.send_keys(value)

    def _click(self, el):
        el.click()

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

    def action_chains(self, mothod, selector):
        from selenium.webdriver.common.action_chains import ActionChains
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

    def screenshot(self, filename):
        import os
        file = os.path.join(os.getcwd(),'pics', 'demo1') + "\\" + filename + ".png"
        self.drv.get_screenshot_as_file(file)

    def alert_prompt(self, text):
        import pyautogui as pg
        value = pg.prompt(text)
        return value

    def alert_confirm(self, content, args):
        import pyautogui as pg
        value = pg.confirm(content, buttons=args)
        return value

    def alert_accept(self):
        self.drv.switch_to.alert.accept()

    def alert_dismiss(self):
        self.drv.switch_to.alert.dismiss()

    def script(self, value):
        self.drv.execute_script(value)

    def _refresh(self):
        self.drv.refresh()

    def wait(self, timeout):
        self.drv.implicitly_wait(timeout)

    def _close(self):
        self.drv.close()

    def _quit(self):
        self.drv.quit()