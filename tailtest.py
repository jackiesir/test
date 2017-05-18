import os
import signal
import subprocess
import time


child=subprocess.Popen('ping 10.10.1.254',stdout=subprocess.PIPE,shell=True)
pid=child.pid
print('Popen.pid:'+str(pid))
while True:
    line=child.stdout.readline().strip()
    if line:
        print(line)
    # else:
    #     child.kill()
    #     print('程序退出')
    #     break



# print(child.stdout.read())
# # child.wait()
# print(child.pid)
# print('parent process')
