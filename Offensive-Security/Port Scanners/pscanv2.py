#!/ur/bin/env python

# Author:Gokan Bektas
# Description: This script will check given host's port number is open or not. 

#importing socket library
import socket
#from socket import *

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input('Please enter the target IP: ') #asking user input IP address.
port = int(input('Please enter a port to scan: ')) #asking user input host number to scan.

def portScan(port):
    result = sock.connect_ex((host, port))
    if result == 0:
        print('Print is Open ')
        
    else:
        print('Port is Closed! ')
        
portScan(port) #calling the function