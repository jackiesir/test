import cmath
import matplotlib.pyplot as plt
import numpy as np
#将数据从文件读到列表data里面


with open (r'd:\zrn\fmlazhurealimag2.s2p','r') as f:
    data=f.readlines()

#将data中数据拆分后放入字典s中
#定义空列表S，所有数据读取后存储再列表S
S_all=[]
for i in data[5:]:
    #定义空字典S_line，每一行中freq存储在 S_line['freq']，S_line[11]，S_line[21]
    S_line={}
    data_line=i.split()
    S_line['freq']=float(data_line[0])
    S_line[11]=complex(float(data_line[1]),float(data_line[2]))
    S_line[21]=complex(float(data_line[3]),float(data_line[4]))
    S_line[12]=complex(float(data_line[5]),float(data_line[6]))
    S_line[22]=complex(float(data_line[7]),float(data_line[8]))
    S_all.append(S_line)

#数据处理部分
C=3e8
fre=[]
ur1=[]
ur2=[]
er1=[]
er2=[]
er3=[]

for s in S_all:
    fre.append(s['freq'])
    d=0.01
    right=15
    L1=(100-right)/1000-d
    L2=right/1000
    L=d
    m=0
    k= (2 * cmath.pi * s['freq']) / C
    s11=s[11] * cmath.exp(-2 * k * L1)
    s21=s[21] * cmath.exp( k * L)
    s12=s[12] * cmath.exp( k * L)
    s22=s[22] * cmath.exp( 2 * k * ( L1+L))

    b=0.0035
    a=0.0015
    U0=1.2566370614e-6
    E0=8.854187817e-12
    UU=U0/E0
    Z0=(cmath.log(b/a)*cmath.sqrt(UU))/(2 *cmath.pi)

    S11=cmath.sqrt( s11 * s21 ) * cmath.exp( -k * L )
    S21=(( s11 + s21 ) * cmath.exp( -k * L ))/2

    ZS1=(Z0 * (1- S11 ** 2 + S21 ** 2 ))/((1-S11) ** 2 - S21 ** 2 )
    ZS2=(Z0 * ((1+ S11) ** 2 - S21 ** 2 ))/ (1- S11 ** 2 + S21 ** 2 )

    Z= cmath.sqrt(ZS1 * ZS2)



    BR=cmath.sqrt(ZS2 / ZS1)
    R=((cmath.tanh(BR) ** -1) + (m*cmath.pi)*1j)/L
    ur1.append((Z/Z0)*(R/k))
    ur2.append((Z/Z0) ** 2)
    er1.append((Z0/Z)*(R/k))
    er2.append((Z0/Z) ** 2)
    er3.append((R/k) ** 2)



#在当前绘图对象中画图，
plt.plot(fre,er1,label='$er1$',color='red',linewidth=1)
plt.plot(fre,er2,label='$er2$',color='blue',linewidth=1)
plt.plot(fre,er3,label='$er3$',color='green',linewidth=1)
# plt.plot(fre,ur2,label='$ur2$',color='black',linewidth=1)

#x轴的文字
plt.xlabel('frequent')

#y轴的文字
plt.ylabel('Eps')

#图标的标题
plt.title('Real Eps')

#x轴的范围
# plt.xlim(0,2)

#y轴的范围
# plt.ylim(0,8)

#显示图示
plt.legend()

#显示图
plt.show()

#保存图
#plt.savefig(r'd:\zrn\RealEps.jpg')

