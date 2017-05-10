#####素数的方法一
'''
方法一使用传统的while循环来实现素数的查找
'''
def showMaxFactor(num):
    count=num//2
    while count>1:
        if num % count==0:
            print('%d的最大约数是%d' % (num,count))
            break
        count -=1
    else:
        print('%d是素数！' % num)

num=int(input('请输入一个数：'))
showMaxFactor((num))

##########素数的方法二
'''
该方法使用for语句的三元操作符和if语句配套使用，简化了语句
'''
x=int(input('请输入一个数：'))
y=[i for i in range(x//2,0,-1) if x%i==0]
print(y)

#斐波那契数列的实现一
def fb1(n):
    a,b=0,1
    z=[]
    while a<n:
        z.append(a)
        a,b=b,a+b
    return z
print(fb1(100))

#zip函数测试
a=[1,2,3,4,5]
b=[9,8,7,6,5]
z=[]
for i,j in zip(a,b):
    z.append(i+j)
print(z)

print(sum(a))