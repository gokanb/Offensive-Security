#!/usr/bin/python

import subprocess
from termcolor import colored


def change_mac_add(interface, mac):
    subprocess.call(["ifconfig " + interface + " down "])
    subprocess.call(["ifconfig " + interface + " hw " + "ether " + mac])
    subprocess.call(["ifconfig " + interface + " up "])
    
def main():
    interface = input('[*]Enter interface to change MAC address on: ')
    new_mac_add = input("[*] Enter  Mac address to change to: ")
    
    before_change = subprocess.check_output(["ifconfig " + interface])
    change_mac_add(interface, new_mac_add)
    after_change = subprocess.check_output(["ifconfig " + interface])
    
    if before_change == after_change:
        print(colored("[!!] Failed to change MAC address to: " + new_mac_add, 'red'))
    else:
        print(colored("[+] MAC address changed to: " + new_mac_add + " on interface " + interface, 'green'))

main()