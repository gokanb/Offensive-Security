#!/ur/bin/env python

# Author:Gokan Bektas
# Description:

import crypt
from termcolor import colored


def crackedPass(cryptWord):
    salt = cryptWord[0:2]
    dictionary = open ('dictionary.txt', 'r')
    for word in dictionary.readlines():
        word = word.strip('\n')
        cryptPass = crypt.crypt(word, salt)
        if (cryptWord == cryptPass):
            print(colored('[+] Found password: ' + word, 'white'))
            return
    print(colored('[-] Password not found! ', 'red'))
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