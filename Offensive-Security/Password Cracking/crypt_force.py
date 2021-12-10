#!/ur/bin/env python

'''

# Author: Gokan Bektas
# Description:
                         ########################## Educational Purpose !!! ##########################
# This script will use bruteforce to crack username and passwords thru using dictonary.txt store and pass1.txt store! 
# Script have couple of python libraries. Crytp crypt. crypt(password) will return the hash of password. 
# You store the hash instead of the clear text password. 
# That way, you can't lose the password to a hacker because you don't have it.

'''

# importing libraries
import crypt                        
from termcolor import colored       

# Function 
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