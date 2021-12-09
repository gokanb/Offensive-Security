#!/ur/bin/env python

# Author:Gokan Bektas
# Description: 

import ftplib

def annonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'anonymous')
        print("[*] " + hostname + "FTP Anonymous Logon Succedeed! ")
        ftp.quit()
        return True
    
    except Exception as e:
        print('[-] ' + hostname + "FTP Anonymous Logon Failed")
        
host = input("Enter an target IP: ")
annonLogin(host)