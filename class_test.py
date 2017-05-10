# class AA:
#     pass
#
# aa=AA()
#
# __metaclass__=type
# class person:
#     def __init__(self,name):
#         self.name=name
#     def getName(self):
#         return self.name
#     def color(self,color):
#         print('%s is %s' % (self.name,color))
# bb=person('chjb')
# #bb.name='chjb'
# bb.color('white')
# print(bb.name)
#
# class ball:
#     def __init__(self,kk):
#         self.name=kk
#     def setName(self,name):
#         self.name=name
#     def kick(self):
#         print("我叫%s,该死的，睢踢我！" % self.name)
# a=ball('aa')
# a.setName('chjb')
# b=ball('bb')
# b.setName('wxj')
# c=ball('cc')
# c.setName('ww')
# a.kick()
# b.kick()
# c.kick()
# d=ball('kk')
# d.kick()
#
#
# class Parent:
#     def hello(self):
#         print('正在调用父类')
# class child(Parent):
#     pass
# c=child()
# c.hello()
#
# import random as r
# class Fish:
#     def __init__(self):
#         self.x=r.randint(0,10)
#         self.y=r.randint(0,10)
#     def move(self):
#         self.x-=1
#         print('我的位置是:%s,%s' % (self.x,self.y))
# class Goldfish(Fish):
#     pass
# class Carp(Fish):
#     pass
# class Saleon(Fish):
#     pass
# class Shark(Fish):
#     def __init__(self):
#         # Fish.__init__(self)
#         super().__init__()
#         self.hungry=True
#     def cat(self):
#         if self.hungry:
#             print("吃货的梦想就是天天有的吃！")
#             self.hungry=False
#         else:
#             print("太累了，吃不了了！")
# fish=Fish()
# fish.move()
# fish.move()
# fish.move()
# fish.move()
# fish.move()
#
# goldfish=Goldfish()
# goldfish.move()
# goldfish.move()
# goldfish.move()
# print('-------------')
# shark=Shark()
# shark.move()
# shark.move()

'''
多重继承实例，尽量少用多重继承；
'''
# class Base1:
#     def foo1(self):
#         print('我是fool，我为base1代言')
# class Base2:
#     def foo2(self):
#         print('我是foo2，我为base2代言')
#
# class c(Base1,Base2):
#     pass
#
# c=c()
# c.foo1()
# c.foo2()
#
# '''
# 组合，将多个类组合在一起
# '''
#
# class Turtle:
#     def __init__(self,x):
#         print('aaaa')
#         self.num=x
# class Fish:
#     def __init__(self,x):
#         self.num=x
# class Pool:
#     def __init__(self,x,y):
#         self.tutle=Turtle(x)
#         self.fish=Fish(y)
#     def print_num(self):
#         print('水池里面总共有乌龟%s只，小鱼%s条!' % (self.tutle.num,self.fish.num))
#
#
# print('-------------')
# pool=Pool(1,10)
# pool.print_num()
#
# t=Turtle(10)
#
# class Rectangle:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def getPeri(self):
#         return (self.x  + self.y)*2
#     def getArea(self):
#         return (self.x*self.y)
# rect=Rectangle(3,4)
# print(rect.getPeri())
# print(rect.getArea())
#
# class CapStr(str):
#     def __new__(cls,string):
#         string=string.upper()
#         return str.__new__(cls,string)
#
# a=CapStr('i am chjb!')
# print(a)
#
# class C:
#     def __init__(self):
#         print('我被调用了！')
#     def __del__(self):
#         print('我被删除了！')
#
# c1=C()
# print('---------------')
# c2=c1
# print('-----------------')
# c3=c2
#
#
#
# print('------------------------')
#
# class New_int(int):
#     def __add__(self, other):
#         return int.__sub__(self,other)
#     def __sub__(self, y):
#         return int.__add__(self,y)
#
# a=New_int('3')
# b=New_int(4)
#
# print(a+b)
# print(a-b)
#
# class int(int):
#     def __add__(self, other):
#         return int.__sub__(self,other)
# a=5
# b=int(3)
# print(b+a)
#
# print(b+1)
#

import time as t

class MyTimer():
    #初始化变量
    def __init__(self):
        self.unit=['年','月','天','小时','分钟','秒']
        self.prompt='未开始计时'
        self.lasted=[]
        self.begin=0
        self.end=0

    def __str__(self):
        return self.prompt

    __repr__=__str__

    def __add__(self, other):
        prompt='总共运行了：'
        result=[]
        for index in range(6):
            result.append(self.lasted[index]+other.lasted[index])
            if result[index]:
                prompt+=(str(result[index])+self.unit[index])
        return prompt

    #开始计时
    def start(self):
        self.begin=t.localtime()
        self.prompt='提示：请先调用stop()停止计时！'
        print('计时开始...')
    #停止计时
    def stop(self):
        if not self.begin:
            print('提示：请先调用start()进行计时！')
        else:
            self.end=t.localtime()
            self._calc()
            print('计时结束！')


    #计算时间
    def _calc(self):
        # self.lasted=[]
        self.prompt='总共运行了：'
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
            if self.lasted[index]:
                self.prompt+=(str(self.lasted[index])+self.unit[index])
        self.lasted=[]
        self.begin=0
        self.end=0