import requests
import os

url='http://www.ynnu.edu.cn/__local/5/62/63/3B7D375692ABA85C0A387AC3738_EE62C835_13E00.jpg'
root=r'd:/chjb/'
path=root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r=requests.get(url)
        r.status_code
        with open(path,'wb') as f:
            f.write(r.content)
            print('文件保存成功！')
    else:
        print('文件已经存在！')
except:
    print('爬取失败！')