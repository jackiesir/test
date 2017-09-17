import requests
from bs4 import BeautifulSoup
import bs4
import re

# url='http://www.ynnu.edu.cn'
#
# def getHtml(url):
#     try:
#         User_agent = {'user-agent': 'Mozilla/5.0'}
#         r = requests.get(url, headers=User_agent, timeout=30)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return '页面获取失败'
#
#
# def test():
#     html=getHtml(url)
#     soup=BeautifulSoup(html,'html.parser')
#     print(soup.text)
#
# test()

match=re.search(r'[1-9]\d{5}','BIT 100081 121212 312123 BIT 100082 211231 23')
if match:
    print(match.group(0))
    # print(match.group(1))

match=re.match(r'[1-9]\d{5}','100081 BIT ')
if match:
    print(match.group(0))

ls=re.findall(r'[1-9]\d{5}','BIT 100081123121111111 BIT 10008232123131')
print(ls)