'''
简单写一个如何爬取图片
下载到demo2文件夹中
'''
import os
import requests
from parsel import Selector

class SpiderPics:
    def __init__(self):
        self.url = 'http://pic.netbian.com/4kfengjing/'
        self.file = os.path.join(os.getcwd(), 'pics', 'demo2')
        self.res = self.get_url()

    def get_url(self):
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363"}
        res = requests.get(self.url, headers=headers)
        #res.encoding="utf-8"
        res.encoding = res.apparent_encoding
        return res
    
    def text(self):
        text = Selector(self.res.text)
        return text

    def content(self, url):
        content = requests.get(url).content
        return content

    def download(self, file, url):
        content = self.content(url)
        with open(file, 'wb') as f:
            f.write(content)

    def main(self):
        pages_sel = ".slist > ul > li"
        pages = self.text().css(pages_sel)
        for page in pages:
            title = page.css("a > b::text").get()
            url = "http://pic.netbian.com" + page.css("a > img::attr(src)").get()
            file = self.file + "\\" + title + '.jpg'
            print(file)
            self.download(file, url)

if __name__ == "__main__":
    s = SpiderPics()
    s.main()