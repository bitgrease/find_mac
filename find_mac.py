import statistics
import paramiko
import sys
import time

if len(sys.argv) < 3:
    sys.exit("You must supply an IP and MAC address as arguments.")

username = 'test'
password = 'test'

ip, mac = sys.argv[1:3]
ssh_pre = paramiko.SSHClient()
ssh_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh_pre.connect(ip, username=username, password=password)
ssh = ssh_pre.invoke_shell()
ssh.send(f"sh mac addr | i {mac}\n")
time.sleep(3)
output = ssh.recv(65535).decode('utf-8')
ssh.close()

with open('mac.txt', 'w') as f:
    f.write(output)

