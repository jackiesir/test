import re

a='10.19.3.40 - - [09/Jun/2017:11:22:20 +0800] GET /system/resource/code/datainput.jsp?owner=1218553039&e=1&w=1440&h=900&treeid=1101&refer=aHR0cDovL3d3dy55bm51LmVkdS5jbi8%3D&pagename=L2NvbnRlbnQuanNw&newsid=16673 HTTP/1.1  200 0  http://www.ynnu.edu.cn/info/1101/16673.htm   Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E) '

#m=re.match( "\d+\.\d+\.\d+\.\d+",a)                     #匹配ip
#m=re.match( r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",a)    #匹配ip
#m=re.findall( r'\w+.ynnu.edu.cn',a)
m=re.findall(r'\w+.ynnu.edu.cn',a)
print(m)