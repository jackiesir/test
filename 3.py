import paramiko

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('202.203.225.46',username='xxglcadmin',password='aaa')
cmd='ls -l'
stdin,stdout,stderr=ssh.exec_command('cd /var/log/nginx')
stdin,stdout,stderr=ssh.exec_command(cmd)
for std in stdout.readlines():
    print(std)
for std in stderr.readlines():
    print(std)
# for std in stdin.readlines():
#     print(std)
ssh.close()