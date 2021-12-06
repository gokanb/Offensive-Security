#!/ur/bin/env python

# Author:Gokan Bektas
# Description: This script will print ask user input target ip and print out 
# how many port it has and show what protocol.

import socket

def retBanner(ip, host):
    try:
        socket.setdefaulttimeout(2)
        sock = socket.socket()
        sock.connect((ip, host))
        banner = sock.recv(1024)
        return banner
    
    except:
        return

def main():
    ip = input('Enter Target IP: ')
    for port in range(20, 1000):
        banner = retBanner(ip,port)
        if banner:
            print(f'[+]Host @ {ip} has port {str(port)} with protocol {str(banner).strip("b")} ')

main()