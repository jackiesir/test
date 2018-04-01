import os
import os.path
l=[]
def get_py(path,l):
    filelist=os.listdir(path)
    for filename in filelist:
        pathTmp=os.path.join(path,filename)
        if os.path.isdir(pathTmp):
            get_py(pathTmp,l)
        elif filename[-3:].upper()=='.PY':
            l.append(pathTmp)
path=input('请输入路径：').strip()
get_py(path,l)
print('在%s目录及其子目录下找到%d个py文件\n分别为：\n'%(path,len(1)))
for filepath in l:
    print(filepath + '\n')
