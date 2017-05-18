import urllib.request
import urllib.parse
import json
import bs4

url='http://fy.iciba.com/ajax.php?a=fy'
my_content=input('请输入要翻译的文本：')

data={ \
    'f':'auto',\
    't':'auto',\
    'w':'I am chinese'\
    }
data['w']=my_content

head={}
head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'
'''
另外headers的一些属性，下面的需要特别注意一下：

    User-Agent : 有些服务器或 Proxy 会通过该值来判断是否是浏览器发出的请求
    Content-Type : 在使用 REST 接口时，服务器会检查该值，用来确定 HTTP Body 中的内容该怎样解析。
    application/xml ： 在 XML RPC，如 RESTful/SOAP 调用时使用
    application/json ： 在 JSON RPC 调用时使用
    application/x-www-form-urlencoded ： 浏览器提交 Web 表单时使用
    在使用服务器提供的 RESTful 或 SOAP 服务时， Content-Type 设置错误会导致服务器拒绝服务

其他的有必要的可以审查浏览器的headers内容，在构建时写入同样的数据即可。
'''
data = urllib.parse.urlencode(data).encode('utf-8')
req=urllib.request.Request(url,data,head)

response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
target=json.loads(html)
if target['status']==1:
    print('翻译结果为：%s'% (target['content']['out'][:-5]))
elif target['status']==0:
    #print(target)
    print('翻译结果为：%s'% (target['content']['word_mean'][0]))
