import re
import datetime
import os
with open (r'D:\testlog\access.log','r') as f:
    log_data=f.readlines()

#获取配置文件里面所有的域名，并保存在列表里面
url_ip_count={}
#创建空字典，用于为url_ip_count的键值赋空字典值
temp_IP=set()
#定义时间差值变量time_interval,秒为单位，并定义两个时间变量。
time_interval=2
time1=datetime.datetime.now()
time2=datetime.datetime.now()

for ynnuURL in os.listdir(r'D:\testlog\sites-enabled'):
    if ynnuURL not in url_ip_count:
            url_ip_count[ynnuURL]=temp_IP.copy()

#203.208.60.230
ipP = r"?P<ip>[\d.]*";

#[21/Jan/2011:15:04:41 +0800]
timeP = r"""?P<time>\[           #以[开始
            [^\[\]]* #除[]以外的任意字符  防止匹配上下个[]项目(也可以使用非贪婪匹配*?)  不在中括号里的.可以匹配换行外的任意字符  *这样地重复是"贪婪的“ 表达式引擎会试着重复尽可能多的次数。
            \]           #以]结束
        """

#"GET /EntpShop.do?method=view&shop_id=391796 HTTP/1.1"
requestP = r"""?P<request>\"          #以"开始
            [^\"]* #除双引号以外的任意字符 防止匹配上下个""项目(也可以使用非贪婪匹配*?)
            \"          #以"结束
            """

statusP = r"?P<status>\d+"

bodyBytesSentP = r"?P<bodyByteSent>\d+"

"http://test.myweb.com/myAction.do?method=view&mod_id=&id=1346"
referP = r"""?P<refer>\"          #以"开始
            [^\"]* #除双引号以外的任意字符 防止匹配上下个""项目(也可以使用非贪婪匹配*?)
            \"          #以"结束
        """
# referP =r'http'
#"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"'
userAgentP = r"""?P<userAgent>\"              #以"开始
        [^\"]* #除双引号以外的任意字符 防止匹配上下个""项目(也可以使用非贪婪匹配*?)
        \"              #以"结束
            """

#原理：主要通过空格和-来区分各不同项目，各项目内部写各自的匹配表达式
nginxLogPattern = re.compile(r"(%s)\ -\ -\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)" %(ipP, timeP, requestP, statusP, bodyBytesSentP, referP, userAgentP), re.VERBOSE)



# m = re.findall(p, data)
count=0
#创建空字典，url_ip_count，字典关键字用域名，value值用一个IP地址组成的集合，采用集合是因为集合里面的值是不能重复的


for data in log_data:
    # count+=1
    # if count>10000:
    #     break
    matchs = nginxLogPattern.match(data)
    if matchs!=None:
        allGroups = matchs.groups()
        ip = allGroups[0]
        #time = allGroups[1]
        #request = allGroups[2]
        #status =  allGroups[3]
        #bodyBytesSent = allGroups[4]
        refer = allGroups[5]
        #userAgent = allGroups[6]
        if '.ynnu.edu.cn' in refer:
            ynnuURL=refer.split('.ynnu.edu.cn')[0].split('//')[1]+'.ynnu.edu.cn' if '://' in refer else refer.split('.ynnu.edu.cn')[0] + '.ynnu.edu.cn'
            # url_ip_count[ynnuURL].add(ip)
            if ynnuURL in url_ip_count:
                url_ip_count[ynnuURL].add(ip)
                time2=datetime.datetime.now()
                if (time2-time1).seconds>time_interval:
                    time1=datetime.datetime.now()
                    for i in url_ip_count:
                        print(i,len(url_ip_count[i]))
                        url_ip_count[i].clear()



# print(url_ip_count)
for i in url_ip_count:
    print(i,len(url_ip_count[i]))

#写文件代码
with open(r'd:/access.txt','w') as f:
    for i in url_ip_count:
        f.write(i+' '+str(len(url_ip_count[i]))+'\n')
# for i in url_ip_count['jwc.ynnu.edu.cn']:
#     print(i)
        # userAgent = matchs.group("userAgent")
        # print(refer)
        # print(userAgent)

        #统计HTTP状态码的数量
        # GetResponseStatusCount(userAgent)
        #在这里补充其他任何需要的分析代码
