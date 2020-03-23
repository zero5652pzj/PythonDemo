'''
'''
import os
from cases.base import Base
from utils.tools import save

class SpiderFiction(Base):
    def __init__(self):
        super().__init__()
        self.drv = self.driver()

    def open_page(self):
        self.drv.get("http://www.booksky.cc/")
        self.max_window()

    def step1(self):
        u'''
        打开小说网站，并在弹窗中输入想要赏阅的小说
        并点击排首位的，进入该小说的页面
        '''
        self.open_page()
        value = self.alert_prompt('请您输入小说名称...')
        if value==None:
            self.quit()
        self.name("searchkey", '输入', value)
        self.class_name("searchbtn", '点击')
        while True:
            #先判断是否有搜索结果
            librarylist = self.drv.find_elements_by_css_selector("body > section > div > div.w-left > div > div.body > ul >li")
            if len(librarylist) == 0:
                value = self.alert_prompt('很遗憾找不到，请您重新输入名称...')
                self.name("searchkey", '输入', value)
                self.class_name("searchbtn", '点击')
            else:
                self.css('body > section > div > div.w-left > div > div.body > ul > li:nth-child(1) > div.pt-ll-r > p.info > span:nth-child(1) > a','点击')
                break

    def step2(self):
        u'''第二步'''
        value = self.alert_confirm('请您选择想要阅读的章节...', ['最新章节', '指定章节', '返回上一页'])
        if value == '最新章节':
            new_title = self.css("body > section > div.container.clearfix.mt20 > div.clearfix > div.w-left > div:nth-child(1) > div.body.novel > div.novelinfo > div.novelinfo-l > ul > li:nth-child(6) > a").text
            self.css("body > section > div.container.clearfix.mt20 > div.clearfix > div.w-left > div:nth-child(1) > div.body.novel > div.novelinfo > div.novelinfo-l > ul > li:nth-child(6) > a", '点击')
            self.change_handle(new_title)
            text = self.css("#chaptercontent").text
            file = os.path.join(os.getcwd(), 'pics', 'demo3') + '\\' + new_title + '.txt'
            save(file, text)
            self.close()
        elif value == '指定章节':
            self.css("body > section > div.container.clearfix.mt20 > div.card.mt20.fulldir > div.body > ul > li.fulltip", "点击")
            value = self.alert_prompt("请输入章节....")
            #这个搜寻范围大，需要时间长，主要是为了实现功能
            chapters = self.drv.find_elements_by_css_selector(".card.fulldir > .body > ul.dirlist.three.clearfix > li")
            for chapter in chapters:
                if value in chapter.text:
                    search_title = chapter.text
                    chapter.click()
                    break
            self.wait(5)
            self.change_handle(search_title)
            text = self.css("#chaptercontent").text
            file = os.path.join(os.getcwd(), 'pics', 'demo3') + '\\' + search_title + '.txt'
            save(file, text)
            self.close()
        elif value == '返回上一页':
            self.drv.back()

    def main(self):
        try:
            self.step1()
            self.step2()
        finally:
            self.quit()

if __name__ == "__main__":
    s = SpiderFiction()
    s.main()