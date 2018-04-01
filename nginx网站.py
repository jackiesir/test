import os
import requests
def getHtmlText(url):
    try:
        r=requests.get(url,timeout=50)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return '失败'

filedir='/home/jackie/Downloads/sites-enabled/'
L=os.listdir(filedir)
count=0
server_list=''

for i in L:
    #count=count+1
    with open(filedir+i,'r',encoding='utf-8',errors='ignore') as f:
        temp=f.readlines()
        wai=''
        nei=''
        for j in temp:
            if 'server_name' in j:

                wai=getHtmlText('http://'+j.split(' ')[-1].strip()[:-1])
                server_list=j.split(' ')[-1].strip()[:-1]+'---'
            if '#proxy_pass' in j:
                break
            if "proxy_pass" in j:
                nei=getHtmlText(j.split(' ')[-1].strip()[:-1])
                server_list=server_list+j.split(' ')[-1].strip()[:-1]
        # if wai=='失败' and nei !='失败':
        #     print(count,server_list)
        if wai=='失败':
            count = count + 1
            print(count,server_list)


