#!/ur/bin/env python
# Author: Gokan Bektas
# Description: 


import socket
import pyfiglet
import sys

banner = pyfiglet.figlet_format(' PORT SCANNER ' )
print(banner) 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host = input('Please enter the target IP: ') #asking user input IP address.
#port = int(input('Please enter a port to scan: '))
targetIP = input('Please enter the target IP: ')

try:
    for i in range(1, 3):
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

def portScan(port):
    result = sock.connect_ex((host, port))
    if result == 0:
        print('Print is Open ')
        
    else:
        print('Port is Closed! ')
        
portScan(port)


    
    
