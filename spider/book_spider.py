#!/usr/bin/env python
# coding=utf-8

from urllib import request
from bs4 import BeautifulSoup

def load_page(url):
    user_agent = 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    headers = {'User_Agent' : user_agent}
    req = request.Request(url, headers = headers)
    response = request.urlopen(req)
    return response.read()

def write_to_file(filename, soup_text):
    f = open(filename, 'w')
    for each in soup_text.find_all('p'):
        f.write(each.text)
    f.close()

def RedDream_spider(url, chapter):
    html = load_page(url)
    bs = BeautifulSoup(html, 'html.parser')
    chapter_name = bs.find('h1').text
    print(chapter_name)
    soup_text = bs.find('div', class_ = 'chapter_content')
    path = './honglou/'
    filename = path + str(chapter) + ".%s.txt" % chapter_name
    write_to_file(filename, soup_text)

if __name__ == "__main__":
    base_url = 'http://www.shicimingju.com/book/hongloumeng/'
    for chapter in range(1, 121):
        url = base_url + str(chapter) + '.html' 
        RedDream_spider(url, chapter)
