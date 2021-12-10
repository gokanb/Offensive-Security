#!/ur/bin/env python

'''
# Author: Gokan Bektas
# Description:
                        ########################## Educational Purpose !!! ##########################
 
            --- Before running this application make sure that first, you hash one of the decrypt value from given list 
            from passwords.txt then take that sha1_hash value output and run sha1_hash.py and put output value as a input. ---

# This script will take encrypted sha1hash value and found the decrypted value in given list passwords.txt and print out. 
'''

# from urllib.request import urlopen
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
        quit()
    else:
        print(colored('[-] Password guess: ' + str(password) + ' does not match, trying next...', 'red'))
        
print('Password not in the password list!') 

        