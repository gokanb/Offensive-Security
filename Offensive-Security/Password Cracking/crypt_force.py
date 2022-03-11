#!/usr/bin/env python

'''
# Author: Gokan Bektas
# Description:
# Date: 
# Version: 1.2
                         ########################## Educational Purpose !!! ##########################
                         
# This script will use bruteforce to crack the password. Will find and print out decrypted password in given list dictionary.txt 
and brute force loop and find correct password for given username and encrypted password. We are passing two different file. 
When password found then will print out red. 

---pass1.txt stores username and password. 
---dictionary.txt stores password.

'''

# importing libraries
import crypt             
from termcolor import colored                  # termcolor will help print out as given colored.

def crackedPass(cryptWord): 
    salt = cryptWord[0:2]                      # Salt is a configuration management and orchestration tool.                                      
    dictionary = open ('dictionary.txt', 'r')  # open dictionary.txt   'r' refers for read.                       
    for word in dictionary.readlines():        # for loop iterate to read line by line.
        word = word.strip('\n')
        cryptPass = crypt.crypt(word, salt)
        if (cryptWord == cryptPass):
            print(colored('[+] Found password: ' + word, 'red'))
            return
    print(colored('[-] Password not found! ', 'white'))
    return

def main():
    passFile = open('pass1.txt', 'r')
    for line in passFile.readlines():          # i used for loop iterate to read line by line. 
        if ":" in line:
            user = line.split(':')[0]          # split line, before : is user, after : is password. [0] refers to first position.  
            cryptWord = line.split(':')[1].strip('').strip('\n')
            #print(cryptWord)
            print('[+] Cracking password for: ' + user)
            crackedPass(cryptWord)
    
main()