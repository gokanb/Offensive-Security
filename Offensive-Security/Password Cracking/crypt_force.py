#!/ur/bin/env python

'''
# Author: Gokan Bektas
# Description:
                         ########################## Educational Purpose !!! ##########################
                         
# This script will use bruteforce to find the password. will find and print out decrypted password in given list dictionary.txt 

---pass1.txt stores username and password. 
---dictionary.txt stores password.
'''

# importing libraries
import crypt                        
from termcolor import colored       

def crackedPass(cryptWord): 
    salt = cryptWord[0:2]                      #                                       
    dictionary = open ('dictionary.txt', 'r')  # open dictionary.txt   'r' refers for read.                       
    for word in dictionary.readlines():
        word = word.strip('\n')
        cryptPass = crypt.crypt(word, salt)
        if (cryptWord == cryptPass):
            print(colored('[+] Found password: ' + word, 'red'))
            return
    print(colored('[-] Password not found! ', 'white'))
    return

def main():
    passFile = open('pass1.txt', 'r')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptWord = line.split(':')[1].strip('').strip('\n')
            #print(cryptWord)
            print('[+] Cracking password for: ' + user)
            crackedPass(cryptWord)
    
main()