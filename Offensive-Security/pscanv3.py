#!/ur/bin/env python

# Author:Gokan Bektas
# Description: 

#importing libraries
import socket
import pyfiglet
import sys

banner = pyfiglet.figlet_format(' PORT SCANNER ')
print(banner)  #import banner to make looks fancy

# if len(sys.argv) == 2: 
#     targetIP = socket.gethostbyname(sys.argv[1])
#     print(targetIP)
# else:
#     print('Invalid argument')
    
targetIP = input('Please enter the target IP: ')

try:
    for i in range(1, 50):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((targetIP, i))
        if result == 0:
            print(f'Port {i} is open: ')
            sock.close()
            
except KeyboardInterrupt:
    print('\n Exiting Now...! ')
    sys.exit()


except socket.gaierror:
    print('\n Host cannot be reached')
    sys.exit()
    
    
except socket.error:
    print('\n Server not responding')
    sys.exit()