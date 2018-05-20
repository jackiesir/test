# import math
# import cmath
# import numpy as np
# import pandas as pd




# def a(x):
#     return x*x
#
# c=[1,2,3,4]
#
# d=list(map(a,c))
# print(d)
#
# print(list(map(str,c)))
#
# from functools import reduce
#
# print(reduce(a,c))
# import cmath
# x=5
#
# a=12 + (12 *x)*1j
# print(a)
# print(type(a))
#
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# x=np.linspace(-10,10,10000)
# y1=np.sin(x)
# y2=np.sinh(x)
# #在当前绘图对象中画图，
# plt.plot(x,y1,label='$sin(x)$',color='red',linewidth=1)
# # plt.plot(x,y2,label='$sinh(x)$',color='blue',linewidth=1)
#
#
# #x轴的文字
# plt.xlabel('x坐标')
#
# #y轴的文字
# plt.ylabel('y坐标')
#
# #图标的标题
# plt.title('函数图像')
#
# #x轴的范围
# # plt.xlim(0,2)
#
# #y轴的范围
# # plt.ylim(0,8)
#
# #显示图示
# plt.legend()
#
# #显示图
# plt.show()



# x=-121
# y=12
#
# c=complex(x,y)
# d=x+y*1j
#
# if c.real<0:
#     c=math.fabs(c.real)+math.fabs(c.imag)*1j
# c.real
# c.imag
# print(c)
# print(c==d)
# print(math.fabs(-0.121))
#
# print(cmath.log(c))
# print(cmath.log(c,10))
# print(cmath.log10(c))

#
# a=[
#     [1,2,3,4,5],
#     [2,3,4,5,6],
#     [7,8,9,1,8]
#     ]
#
# b=[
#     [2,3,4,2,3],
#     [4,3,2,2,3],
#     [2,3,1,2,3]
#     ]
# print(a)
# a=np.array(a)
# b=np.array(b)
# a=np.mat(a)
# b=np.mat(b)
# print(type(a))
# print(type(b))
# print(a)
# print(a*b)
# print(np.min(a*b))
#
# count=0
# while True:
#     print(count)
#     count+=1
#     if count>10:
#         break
#
#
# data_line=[b'10.74.36.5', b'-', b'-', b'[02/Jun/2017:08:54:23', b'+0800]', b'"GET', b'/system/resource/style/component/news/content/title.css', b'HTTP/1.1"', b'304', b'0', b'"http://it.ynnu.edu.cn/info/1043/1461.htm"', b'"Mozilla/4.0', b'(compatible;', b'MSIE', b'7.0;', b'Windows', b'NT', b'6.1;', b'WOW64;', b'Trident/5.0;', b'SLCC2;', b'.NET', b'CLR', b'2.0.50727;', b'.NET', b'CLR', b'3.5.30729;', b'.NET', b'CLR', b'3.0.30729;', b'.NET4.0C;', b'.NET4.0E)"']
#
# print('IP：',data_line[0].decode(),'时间：',data_line[3].decode()[1:],'访问页面：',data_line[6].decode(),'访问域名：',data_line[10].decode().split('/')[2])
# print(type(data_line[0]))

# a=-1+2j
# print(abs(a))

#
#
# import sympy as spy
# def f(x):
#     return (x-3)**3 #''定义f(x) = (x-3）**3'''
#
# def fd(x):
#     # return 3*((x-3)**2)#''定义f'(x) = 3*((x-3）**2）
#     x=spy.Symbol('x')
#     return spy.diff(f(x),x)
# # f1=np.diff(f)
#
#
# def newtonMethod(n,assum):
#     time = n
#     x = assum
#     Next = 0
#     A = f(x)
#     # B = fd(x)
#     x=spy.Symbol('x')
#     B=spy.diff(f(x),x)
#     print('A = ' + str(A) + ',B = ' + str(B) + ',time = ' + str(time))
#     if f(x) == 0.0:
#         return time,x
#     else:
#         Next = (x - A/B)
#         print('Next x = '+ str(Next))
#     if A == f(Next):
#         print('Meet f(x) = 0,x = ' + str(Next))#''设置迭代跳出条件，同时输出满足f(x) = 0的x值'''
#
#     else:
#         return newtonMethod(n+1,Next)
#
# newtonMethod(0,4) #''设置从0开始计数，x0 = 4.0'''


# y=spy.Symbol('x')
# print(spy.diff(y**3+2*y,y))


# #有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# totlecount=0
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if(i !=k) and (i !=j) and (j!=k):
#                 totlecount+=1
#                 print(totlecount,':',i,j,k)
#
#



# def fib(max):
#     a,b=0,1
#     z=[]
#     while a<max:
#         print(a,end=' ')
#         a,b=b,a+b
#     return z
#
# fib(100000000000000000000000)
import requests
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        # User_agent = {'user-agent': 'Mozilla/5.0'}
        r=requests.get(url, timeout=300)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print('失败')
        return ''

url='http://www.ynnu.edu.cn'

print(getHTMLText(url))