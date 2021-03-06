import cmath
import matplotlib.pyplot as plt
# 导入中文字体显示模块
import pylab
#将数据从文件读到列表data里面
with open (r'd:\zrn\usomteflondbmag.s2p','r') as f:
    data=f.readlines()

#将data中数据拆分后放入字典s中
#定义空列表S，所有数据读取后存储再列表S
S_all=[]
for i in data[0:]:
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
# R的虚部存放在一个字典里面
R_imag = []

m = 0
d = 0.016
right = 15
L1 = (125 - right) / 1000 - d
L2 = right / 1000
L =d
for s in S_all:
    fre.append(s['freq'])
    k= 1j*(2 * cmath.pi * s['freq']) / C
    # s11=s[11] * cmath.exp(2 * k * L1)
    # s21=s[21] * cmath.exp( -k * L)
    # s12=s[12] * cmath.exp( -k * L)
    # s22=s[22] * cmath.exp( -2 * k * ( L1+L))

    s11m=s[11].real*cmath.exp((-1j*s[11].imag*cmath.pi)/180)
    s21m=s[21].real*cmath.exp((-1j*s[21].imag*cmath.pi)/180)
    s12m=s[12].real*cmath.exp((-1j*s[12].imag*cmath.pi)/180)
    s22m=s[22].real*cmath.exp((-1j*s[22].imag*cmath.pi)/180)


    b=0.0035
    a=0.00152
    U0=1.2566370614e-6
    E0=8.854187817e-12
    UU=U0/E0
    Z0=(cmath.log(b/a)*cmath.sqrt(UU))/(2 *cmath.pi)
    S11kk=s11m*cmath.exp(2*k*L1)
    S11=cmath.sqrt( s11m * s22m ) * cmath.exp( -k * L )
    S21=(( s12m + s21m ) * cmath.exp( -k * L ))/2
    if S11kk.real>0 and S11.real<0:
        S11=complex(-S11.real,S11.imag)
    elif S11kk.real<0 and S11.real>0:
        S11=complex(-S11.real,S11.imag)
    ZS1=(Z0 * (1- S11 ** 2 + S21 ** 2 ))/((1-S11) ** 2 - S21 ** 2 )
    ZS2=(Z0 * ((1+ S11) ** 2 - S21 ** 2 ))/ (1- S11 ** 2 + S21 ** 2 )
    Z= cmath.sqrt(ZS1 * ZS2)
    BR=cmath.sqrt(ZS2 / ZS1)
    R=((cmath.tanh(BR) ** -1) + (m*cmath.pi)*1j)/L
    R_imag.append(R.imag)
    if len(R_imag) > 1:
        print(len(R_imag), R_imag, m)
        if R_imag[len(R_imag) - 1] < R_imag[len(R_imag) - 2]:
            m = m +1

    ur1.append((Z/Z0)*(R/k))
    ur2.append(((Z/Z0) ** 2).real)
    er1.append(((Z0/Z)*(R/k)).real)
    er2.append(((Z0/Z) ** 2).real)
    er3.append((R/k) ** 2)
    # print(ur2)

#在当前绘图对象中画图，
plt.plot(fre,er1,label='$er1$',color='red',linewidth=1)
plt.plot(fre,er2,label='$er2$',color='blue',linewidth=1)
plt.plot(fre,ur2,label='$ur2$',color='green',linewidth=1)
# plt.plot(fre,ur2,label='$ur2$',color='black',linewidth=1)

# 定义显示的中文字体
pylab.mpl.rcParams['font.sans-serif'] = ['SimHei']

#x轴的文字
plt.xlabel('fre频率')

#y轴的文字
plt.ylabel('Eps-Y轴')

#图标的标题
plt.title('曲线图')

#x轴的范围
# plt.xlim(0,2)

#y轴的范围
# plt.ylim(0,8)

#显示图示
plt.legend()

# 保存图
#plt.savefig(r'D:\zrn\RealEps.png',fmt='png',dpi=160)

#显示图
plt.show()
