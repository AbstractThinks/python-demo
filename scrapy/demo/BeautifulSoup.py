from urllib.request import urlopen
from bs4 import BeautifulSoup

try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)



bsObj = BeautifulSoup(html.read())
print(bsObj.h1)
# 相同效果
# print(bsObj.html.h1)
# print(bsObj.body.h1)
# print(bsObj.html.body.h1)
