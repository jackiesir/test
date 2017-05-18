import dns.resolver


hosts=['baidu.com','yahoo.com']

def query(host_list=hosts):
    collection=[]
    for host in host_list:
        ip=dns.resolver.query(host,'A')
        for i in ip:
            collection.append(str(i))
    return collection

if __name__=='__main__':
    for arec in query():
        print(arec)


