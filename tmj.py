import os
import xml.dom.minidom as xmldom

from gensim.models import word2vec


xmlfilepath = os.path.abspath('/home/jackie/Documents/tmj/argoData.xml')
DOMTree = xmldom.parse(xmlfilepath)
collection = DOMTree.documentElement
# 获取集合中所有logentry
logentrys = collection.getElementsByTagName("logentry")
# 存放节点里面logentry  revision 的值
p_revision = ''
# 存放节点里面author 的值，以下变量以此类推！

p_author = ''
p_date = ''
p_path_action = ''
p_path = ''
p_msg = ''

# 打开每一个logentry里面的详细信息
for logentry in logentrys:
    if logentry.hasAttribute('revision'):  # 判断logentry下是否有revision这个属性值
        p_revision = logentry.getAttribute('revision') # 获取logentry下是否有revision这个属性值，并保存在p_revision变量中
        print(p_revision,end=' ')
    author = logentry.getElementsByTagName('author')[0]  # 获取logentry下的author元素。
    p_author = author.childNodes[0].data # 获取author的值，并存放再p_author里面
    print(p_author, end=' ')

    date = logentry.getElementsByTagName('date')[0]
    p_date = date.childNodes[0].data
    print(p_date)

    # 因为paths节点下有多个path，for循环获取每一个节点下的所有path
    paths = logentry.getElementsByTagName('paths')[0]
    path = paths.getElementsByTagName('path')
    for path_i in path:
        p_path_action = path_i.getAttribute('action')
        p_path = path_i.childNodes[0].data
        print('----',p_path_action,p_path)

    msg = logentry.getElementsByTagName('msg')[0]
    p_msg = msg.childNodes[0].data
    print(p_msg)
