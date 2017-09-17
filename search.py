#抓取网页通用代码框架
# import requests
# from bs4 import BeautifulSoup
# import time
# def getHTMLText(url):
#     try:
#         kv={'user-agent':'Mozilla/5.0'}
#         r=requests.get(url,headers=kv,timeout=30)
#         r.raise_for_status()
#         r.encoding=r.apparent_encoding
#         return r.text
#     except:
#         return '产生异常'
#
# print(getHTMLText('https://www.amazon.cn/b/ref=lp_1910600071_gbph_img_s-3_547a_1304576a?rh=i%3Aapparel%2Cn%3A1910600071%2Cn%3A1910600071&ie=UTF8&smid=A1AJ19PSB66TGU&node=1910600071'))

#
# kv={'q':'云南师范大学'}
# User_agent={'user-agent':'Mozilla/5.0'}
# try:
#     r=requests.get('http://www.so.com/s',params=kv)
#     r.raise_for_status()
#     r.encoding=r.apparent_encoding
#     print(r.text)
# except:
#     print('产生异常')


# #下载网络图片
# path=r'd:/'
# url='http://www.ynnu.edu.cn/__local/5/62/63/3B7D375692ABA85C0A387AC3738_EE62C835_13E00.jpg'
# r=requests.get(url)
# with open(path + url.split('/')[-1],'wb') as f:
#     f.write(r.content)

# url='http://www.ip138.com/ips138.asp'
# kv={}
# kv['ip']='202.203.223.1'
# kv['action']=2
# try:
#     r=requests.get(url,params=kv)
#     r.raise_for_status()
#     r.encoding=r.apparent_encoding
#     soup=BeautifulSoup(r.text,'html.parser')
#     print(soup.body.contents[9].li.string)
#     print(soup.body.contents[9].li.next_sibling.string)
# except:
#     print('error!')

'''
从网络上获取中国大学的排名内容
程序的结构设计
步骤1：从网络上获取大学排名网页的内容
        getHTMLText()
步骤2：提取网页内容中的信息到合适的数据结构
        fillUnivList()
步骤3：利用数据结构展示并输出结果
        printUnivList()
'''
import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        # User_agent = {'user-agent': 'Mozilla/5.0'}
        r=requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print('失败')
        return ''

def fillUnivList(ulist,html):
    if html!='':
        soup=BeautifulSoup(html,'html.parser')
        for tr in soup.find('tbody').children:
            if isinstance(tr,bs4.element.Tag):
                tds=tr('td')
                ulist.append([str(tds[0]).split('<td>')[1] , tds[1].string , tds[2].string , tds[3].string])
    else:
        print('网页内容没有读取！')


def printUnivList(ulist,num):
    print('{:^10}\t{:^6}\t{:^10}'.format('排名','学校','名次'))
    for i in range(num):
        u=ulist[i]
        print('{:^10}\t{:^6}\t{:^10}'.format(str(ulist[i][0]),str(ulist[i][1]),str(ulist[i][2])))

def main():
    uinfo=[]
    url='http://www.zuihaodaxue.com/zuihaodaxuepaiming2017.html'
    html=getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)

main()
