#!/ur/bin/env python

'''
# Author: Gokan Bektas
# Description:
                        ########################## Educational Purpose !!! ##########################
# This script will take given input string by user and print out as encrypted. 
# There are a few different versions we can get from hashlib library and i've used such as md5, sha1..sha512
# Tip: More you encrypt the more time it takes to decrypt.
'''

# importing libraries 
# hashlib library store may diferent ways of encryption.
# termcolor library will help us out printing out output colored. 
import hashlib                      
from termcolor import colored       


# creating variable as hasvalue holds input to ask user input.
hashvalue = input(colored('Enter a string to hash: '))     


# hash_object1 is our variable that stores = hashlib.md5() in this case 'the version of encrypt is .md5'
# update hashvalue.encode () will encode the string. 
# print() output will print out encrypted value of given string.
# hexidigest returns the encoded data in hexadecimal format.
# colored ('string: ' + variable + 'string:' + arg.() ,  'choosen color') prints as colored.
hash_object1 = hashlib.md5()            
hash_object1.update(hashvalue.encode())  
print(colored('Text: ' + hashvalue + ' with the md5-hashed is converted to: ' + hash_object1.hexdigest(), 'yellow'))


# hash_object2 is our variable that stores = haslib.sha1  in this case 'the version of encrypt is .sha1'
# print() will print out encrypted value of given string in choosen color.
hash_object2 = hashlib.sha1()
hash_object2.update(hashvalue.encode())
print(colored('Text: ' + hashvalue + ' with the sha1-hashed is converted to: ' + hash_object2.hexdigest(), 'red'))

hash_object3 = hashlib.sha224()
hash_object3.update(hashvalue.encode())
print(colored('Text: ' + hashvalue + ' with the sha224-hashed is converted to: ' + hash_object3.hexdigest(), 'magenta'))

hash_object4 = hashlib.sha256()
hash_object4.update(hashvalue.encode())
print(colored('Text: ' + hashvalue + ' with the sha256-hashed is converted to: ' + hash_object4.hexdigest(), 'white'))

hash_object5 = hashlib.sha512()
hash_object5.update(hashvalue.encode())
print(colored('Text: ' + hashvalue + ' with the sha512-hashed is converted to: ' + hash_object5.hexdigest(), 'cyan'))