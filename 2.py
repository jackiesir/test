# #斐波那契数列的实现一
# def fb1(n):
#     a,b=0,1
#     z=[]
#     while a<n:
#         z.append(a)
#         a,b=b,a+b
#     return z
# print(fb1(100))
#
# #斐波那契数列的实现二
# def fb2(n):
#     pass
#
#
# #zip函数测试
# a=[1,2,3,4,5]
# b=[9,8,7,6,5]
# z=[]
# for i,j in zip(a,b):
#     z.append(i+j)
# print(z)
#
# print(sum(a))

#
# a = list(range(100))
# b = list(range(100))
# c = []
# for i in range(len(a)):
#     a[i] = i ** 2
#     b[i] = i ** 3
#     c.append(a[i] + b[i])
# print(c)

# import numpy
# a = numpy.arange(100) ** 2
# b = numpy.arange(100) ** 3
# print(a+b)

import wx
App = wx.App()
win = wx.Frame(parent = None,size = [600,400],title = 'Python窗口开发测试')
win.Show()
App.MainLoop()

