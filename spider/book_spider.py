#!/usr/bin/env python
# coding=utf-8

from urllib import request
from bs4 import BeautifulSoup

class Spider :
    def __init__(self, url, agent, path):
        self.url = url 
        self.agent = agent
        self.path = path
    def load_page(self, url):
        headers = {'User_Agent' : self.agent}
        req = request.Request(url, headers = headers)
        response = request.urlopen(req)
        return response.read()
    def write_to_file(self, filename, soup_text):
        f = open(filename, 'w')
        for each in soup_text.find_all('p'):
            f.write(each.text)
        f.close()

    def bookSpider(self, url, chapter):
        html = self.load_page(url)
        bs = BeautifulSoup(html, 'html.parser')
        chapter_name = bs.find('h1').text
        print(chapter_name)
        soup_text = bs.find('div', class_ = 'chapter_content')
        filename = self.path + str(chapter) + ".%s.txt" % chapter_name
        self.write_to_file(filename, soup_text)

obj = Spider("http://www.shicimingju.com/book/hongloumeng/", "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36", "./honglou/")

if __name__ == "__main__":
    for chapter in range(1, 121):
        burl = obj.url + str(chapter) + '.html'
        obj.bookSpider(burl, chapter)




