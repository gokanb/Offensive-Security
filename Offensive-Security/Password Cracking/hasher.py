#!/ur/bin/env python

# Author:Gokan Bektas
# Description: 

import hashlib
from termcolor import colored


hashvalue = input(colored('Enter a string to hash: '))

hash_object1 = hashlib.md5()
hash_object1.update(hashvalue.encode())
print(colored('Text: ' + hashvalue + ' with the md5-hashed is converted to: ' + hash_object1.hexdigest(), 'yellow'))

hash_object1 = hashlib.sha1()
hash_object1.update(hashvalue.encode())
print(colored('Text: ' + hashvalue + ' with the md5-hashed is converted to: ' + hash_object1.hexdigest(), 'red'))

hash_object1 = hashlib.sha224()
hash_object1.update(hashvalue.encode())
print(colored('Text: ' + hashvalue + ' with the md5-hashed is converted to: ' + hash_object1.hexdigest(), 'yellow'))

hash_object1 = hashlib.sha256()
hash_object1.update(hashvalue.encode())
print(colored('Text: ' + hashvalue + ' with the md5-hashed is converted to: ' + hash_object1.hexdigest(), 'white'))

hash_object1 = hashlib.sha512()
hash_object1.update(hashvalue.encode())
print(colored('Text: ' + hashvalue + ' with the md5-hashed is converted to: ' + hash_object1.hexdigest(), 'cyan'))