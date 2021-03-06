#!/ur/bin/env python
'''
# Author: Gokan Bektas
# Description: This program will scann connection and Ports are of host that open or close.
# Date : 3-10-22
# Version : 1.3

                        ########################## Educational Purpose !!! ##########################
 
'''

#importing libraries 
from socket import *
import argparse
from threading import *
from typing import final
from colorama import Fore, Style #color and style print out. 
import pyfiglet

banner = pyfiglet.figlet_format(' Port     Scanner ')
print(banner)  #import banner to make looks fancy

#Scanning connection of host's that open or close. 
def connScan(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        print(f'[+] {port} /tcp Open')
        
    except:
        print(Fore.RED + f'[-] {port} /tcp Closed')
        
    finally:
        sock.close()

#Scanning ports of host's  that open or close and getting 
def portScan(host, ports):
    try:
        tgIP = gethostbyname(host)
    except:
        print(f'Unknown Host {host}')
        
    try:
        tgtName = gethostbyaddr(tgIP)
        print(f'[+] Scan result for: {tgIP} [0]')
    
    except:
        print(f' [+] Scan result for: {tgIP}')
        
    setdefaulttimeout(1)
    
    for port in ports:
        thread = Thread(target=connScan, args=(host, int(port)))
    
    
def main():
    parser = argparse.ArgumentParser(prog = 'pscanv4.py', usage = '-d sam.com -p 21,22',
    description = 'Scan a port stated target host IP')
    parser.add_argument('-d', '--host', help = 'Specify a target')
    parser.add_argument('-p', '--port', help = 'Specify target ports seperated by coma')
    
    args = parser.parse_args()
    
    host = args.host
    ports = str(args.port).split(',')
    if (host == None) | (ports[0] == None):
        print(parser.usage)
        exit(0)
        
    portScan(host, ports)
    
    
main()

