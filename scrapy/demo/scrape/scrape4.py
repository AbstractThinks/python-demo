# -*- coding: utf-8 -*-
from urllib.request import urlopen
import sys
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        type = sys.getfilesystemencoding()
        bsObj = BeautifulSoup(html.read(), "html.parser").decode('utf-8').encode(type)
        print(bsObj)
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://news.qq.com/")
if title == None:
    print("title could not be found")
else:
    print(title)
