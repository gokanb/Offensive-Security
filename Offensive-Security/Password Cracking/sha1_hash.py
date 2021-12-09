#!/ur/bin/env python

# Author:Gokan Bektas
# Description: 

from urllib.request import urlopen
import hashlib
from termcolor import colored

sha1hash = input('[*] Enter sha1 Hash value: ')

# passlist = str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"))

# for i in passlist.split('\n'):
#     hashguess = hashlib.sha1(bytes(i, 'utf-8')).hexdigest()
#     if hashguess == sha1hash:
#         print(colored('[+] the password is: ' + str(i), 'white'))
#         quit()
#     else:
#         print(colored('[-] Password guess: ' + str(i) + ' does not match, trying next...', 'red'))
        
# print('Password not in the password list!') 

file = open('passwords.txt', 'r')
for password in file.readlines():
    password = password.strip('\n')
    hashguess = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
    if hashguess == sha1hash:
        print(colored('[+] the password is: ' + str(password), 'white'))
    else:
        print(colored('[-] Password guess: ' + str(password) + ' does not match, trying next...', 'red'))
        
print('Password not in the password list!') 

        