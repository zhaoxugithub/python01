# -*-coding:utf-8-*-
import paramiko

host = '192.168.1.152'
port = 22
username = 'root'
key_filename = '/root/.ssh/authorized_keys'

# 创建 SSH 客户端
client = paramiko.SSHClient()

# 允许连接不在 known_hosts 文件中的主机
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 使用私钥进行认证
key = paramiko.RSAKey.from_private_key_file(key_filename)
client.connect(hostname=host, port=port, username=username, pkey=key)

# 执行命令
stdin, stdout, stderr = client.exec_command('ls')

# 输出结果
print(stdout.read().decode())

# 关闭连接
client.close()