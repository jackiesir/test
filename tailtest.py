import subprocess
import re
import os
import datetime
import time

# 获取配置文件里面所有的域名，并保存在列表里面{'it.ynnu.edu.cn': {'10.80.7.1', '10.73.26.9'},'www.ynnu.edu.cn': {'10.80.7.1', '10.73.26.9'}}
url_ip_count = {}
# 创建空字典，用于为url_ip_count的键值赋空字典值
temp_IP = set()
# 定义时间差值变量time_interval,秒为单位，并定义两个时间变量。
time_interval = 300
time1 = datetime.datetime.now()
time2 = datetime.datetime.now()
for ynnuURL in os.listdir(r'/etc/nginx/sites-enabled'):
    if ynnuURL not in url_ip_count:
        url_ip_count[ynnuURL] = temp_IP.copy()

child = subprocess.Popen('tail -f /var/log/nginx/access.log', stdout=subprocess.PIPE, shell=True)
pid=child.pid
count = 0

# 定义正则表达式，把日志中的ip、时间、域名等信息提取出来


# 203.208.60.230
ipP = r"?P<ip>[\d.]*";

# [21/Jan/2011:15:04:41 +0800]
timeP = r"""?P<time>\[           #以[开始
            [^\[\]]* #除[]以外的任意字符  防止匹配上下个[]项目(也可以使用非贪婪匹配*?)  不在中括号里的.可以匹配换行外的任意字符  *这样地重复是"贪婪的“ 表达式引擎会试着重复尽可能多的次数。
            \]           #以]结束
        """

# "GET /EntpShop.do?method=view&shop_id=391796 HTTP/1.1"
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
# "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"'
userAgentP = r"""?P<userAgent>\"              #以"开始
        [^\"]* #除双引号以外的任意字符 防止匹配上下个""项目(也可以使用非贪婪匹配*?)
        \"              #以"结束
            """

# 原理：主要通过空格和-来区分各不同项目，各项目内部写各自的匹配表达式
nginxLogPattern = re.compile(r"(%s)\ -\ -\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)" % (
ipP, timeP, requestP, statusP, bodyBytesSentP, referP, userAgentP), re.VERBOSE)

print('Popen.pid:'+str(pid))
while True:
    line=child.stdout.readline().strip()
    matchs = nginxLogPattern.match(line.decode())
    if matchs != None:
        allGroups = matchs.groups()
        ip = allGroups[0]
        time = allGroups[1]
        request = allGroups[2]
        status = allGroups[3]
        bodyBytesSent = allGroups[4]
        refer = allGroups[5]
        userAgent = allGroups[6]
        if '.ynnu.edu.cn' in refer:
            # 从日志信息里面提取出****.ynnu.edu.cn的信息
            ynnuURL = refer.split('.ynnu.edu.cn')[0].split('//')[1] + '.ynnu.edu.cn' if '://' in refer else \
            refer.split('.ynnu.edu.cn')[0] + '.ynnu.edu.cn'
            # 判断如果提取出的域名在url_ip_count里面，则将ip地址作为元素添加到url_ip_count字典里面与域名为键的值里面
            if ynnuURL in url_ip_count:
                url_ip_count[ynnuURL].add(ip)
                time2 = datetime.datetime.now()
                if (time2 - time1).seconds > time_interval:
                    time1 = datetime.datetime.now()
                    print(time1)
                    print('www.ynnu.edu.cn ', len(url_ip_count['www.ynnu.edu.cn']))
                    print('it.ynnu.edu.cn  ', len(url_ip_count['it.ynnu.edu.cn']))
                    # 将数据写到文件/var/www/html/aua.htm
                    with open(r'/var/www/html/aua.htm', 'w') as f:
                        f.write(str(time1) + '\n')
                        for ynnuURL in os.listdir(r'/etc/nginx/sites-enabled'):
                            f.write(ynnuURL + ' ' + str(len(url_ip_count[ynnuURL])) + '\n')
                    # 将url_ip_count数据清空
                    for i in url_ip_count:
                        # print(i,len(url_ip_count[i]))
                        url_ip_count[i].clear()
                        # if '.ynnu.edu.cn' in refer:
                        #    try:
                        #        ynnuURL=refer.split('.ynnu.edu.cn')[0].split('//')[1]+'.ynnu.edu.cn'
                        #        print(ip,time.split()[0][1:],ynnuURL)
                        #    except IndexError as e:
                        #        print('出错了！',ip,time,refer)
                        #        count+=1
                        #        if count>2:
                        #            break

                        # count+=1
                        #if count >5000:
    #    break
