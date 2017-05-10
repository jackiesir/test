#斐波那契数列的实现一
def fb1(n):
    a,b=0,1
    z=[]
    while a<n:
        z.append(a)
        a,b=b,a+b
    return z
print(fb1(100))

#斐波那契数列的实现二


#zip函数测试
a=[1,2,3,4,5]
b=[9,8,7,6,5]
z=[]
for i,j in zip(a,b):
    z.append(i+j)
print(z)

print(sum(a))