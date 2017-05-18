import urllib.request
import urllib.parse
import json
import bs4
import re
from bs4 import BeautifulSoup
response=urllib.request.urlopen('http://www.ynnu.edu.cn')
html=response.read()


# class YnnuSpider(object):
#     def __init__(self,word,max_link):
#         self._word=word
#         self._max_link=max_link
#         p={'word':word}
#         self._start_url='www.ynnu.edu.cn'

soup=BeautifulSoup(html,"html.parser")

for i in soup.find_all('a',class_='c112246',limit=2):
    print(i.text,'--->','http://www.ynnu.edu.cn/'+i['href'])

# print(soup.find_all('a',class_='c112246'))
# for each in soup.p['class']:
#     print(each)

