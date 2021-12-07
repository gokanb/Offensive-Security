#!/ur/bin/env python
# Author: Gokan Bektas
# Description: This script will check given host's port number is open or not. 


#import library
import socket
#from socket import *
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.123.123'
port = 92

def portScan(port):
    result = sock.connect_ex((host,port))
    if result == 0: #zero refers False 1 refers True
        print('Port is Open')
        
    else:
        print('Port is Closed!')
        
portScan(port) 