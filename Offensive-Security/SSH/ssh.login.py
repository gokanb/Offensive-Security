#!/ur/bin/env python

# Author:Gokan Bektas
# Description: 

import pexpect #allow us to send particular target 

PROMPT = ['# ', '>>> ', '>' '\$ ']

def connect(user, host, password):
    ssh_newkey = "Are you sure you want to continue connecting? "
    connStr = 'ssh ' + user + '@' + host #domain - IP address
    child = pexpect.spawn(connStr) #spawn allows us to send and expect respond... run commands only sends which we dont use here.
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: ']) 
    if ret == 0:
        print('[-] Error Connecting') 
        return
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
        if ret == 0:
            print('[-]Error Connecting')
            return
    child.sendline(password)
    child.expect(PROMPT)
    return child
    
    
def send_command(child, command): #whatever returns from child sends command and expect prompt
    child.sendline(command)
    child.expect(PROMPT)
    print(child.before)
    
    
def main(): 
    host = input("Please enter the host to target: ")
    user = input("Please enter the user to target: ")
    password = input("Please enter the SSH to target: ")
    child = connect(user, host, password)
    #send_command(child, 'sudo cat /etc/shadow | grep root;ps') #commands
    send_command(child, 'ls')


main()

