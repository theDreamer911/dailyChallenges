# Versi 0.1
import paramiko
import sys
import getpass
import time

hostname = '192.168.0.101'  # sys.argv[1]
port = 22
username = 'scarletpark'
password = getpass.getpass()

# memulai koneksi
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
client.connect(hostname, port, username=username, password=password)

for command in 'echo "Hello SSH Server"', 'uname', 'uptime', 'python3 -V':

    stdin,  stdout, stderr = client.exec_command(command)

    stdin.close()

    print(repr(stdout.read()))
    stdout.close()
    stderr.close()

client.close()
