#!/ur/bin/env python

# Author:Gokan Bektas
# Description: 

import socket
import os
import sys
import struct
import binascii

sock_created = False
sniffer_socket = 0

def analyze_udp_header(data_recv):
    udp_hdr = struct.unpack('!4H', data_recv[:8])
    src_port = udp_hdr[0]
    dst_port = udp_hdr [1]
    length =udp_hdr[2]
    checksum = udp_hdr[3]
    data = data_recv [8:]
    
    print('_____UDP HEADER_____')
    print(f'Source: {src_port}')            # string formating from %hu
    print(f'Destination: {dst_port}')
    print(f'Lenght: {udp_hdr}')
    print(f'Checksum: {checksum}')
    
    return data
    
def analyze_tcp_header(data_recv):
    tcp_hdr = struct.unpack('!2H2I4H', data_recv[:20])
    src_port = tcp_hdr[0]
    dst_port = tcp_hdr[1]
    seq_num = tcp_hdr[2]
    ack_num = tcp_hdr[3]
    data_offset = tcp_hdr[4] >> 2
    reserved = (tcp_hdr[5]) >> 6 & 0x03ff
    flags = tcp_hdr[4] & 0x003f
    window = tcp_hdr[5]
    checksum = tcp_hdr[6]
    urg_ptr = tcp_hdr[7]
    data = data_recv[20:]
    
    urg = bool(flags & 0x0020)
    ack = bool(flags & 0x0010)
    psh = bool(flags & 0x0008)
    rst = bool(flags & 0x0004)
    syn = bool(flags & 0x0002)
    fin = bool(flags & 0x0001)
    
    print('__________TCP HEADER__________')
    print(f'Source: {src_port}')                #string formating from %hu
    print(f'Destination: {dst_port}')
    print(f'Seq: {seq_num}')
    print(f'Ack: {ack_num}')
    print('Flags: ')
    print(f'URG: {urg}')
    print(f'ACK: {ack}')
    print(f'PSH: {psh}')
    print(f'RST: {rst}')
    print(f'SYN: {syn}')
    print(f'FIN: {fin}')
    print(f'Winsize: {window}')
    print(f'Checksum: {checksum}')
    
    return data
    
def analyze_ip_header(data_recv):
    '''
    The '6H4s4s' is designed to allow the struct.unpack function to convert the data recieved from the 
    data_recv variable which comes in a long string of data and needs to be broken down to be interpreted
    and integrated for usage!
    To learn more check out the command 'scapy', then 'ls(IP)' and check out the fields.
    Search and check out the 'ip header structure' for more understanding on IP heaxer and protocols.
    '''
    
    ip_hdr = struct.unpack('!6H4s4s', data_recv[:20])
    ver = ip_hdr[0] >> 12
    ihl = (ip_hdr[0] >> 8) & 0x0f
    tos = ip_hdr[0] & 0x00ff
    tot_len = ip_hdr[1]
    ip_id = ip_hdr[2]
    flags = ip_hdr[3] >> 13
    frag_offset = ip_hdr[3] & 0x1fff
    ip_ttl = ip_hdr[4] >> 8
    ip_proto = ip_hdr[4] & 0x00ff
    checksum = ip_hdr[5]
    src_address = socket.inet_ntoa(ip_hdr[6])
    dst_address = socket.inet_ntoa(ip_hdr[7])
    data = data_recv[20:]
    
    print('__________IP HEADER__________')
    print(f'Version: {ver}')                    #string formating from %hu
    print(f'IHL: {ihl}')
    print(f'TOS: {tos}')
    print(f'Length: {tot_len}')
    print(f'ID: {ip_id}')
    print(f'Offset: {frag_offset}')
    print(f'TTl: {ip_ttl}')
    print(f'Proto: {ip_proto}')
    print(f'Checksum: {checksum}')
    print(f'Source IP: {src_address}')          #string formating from %s
    print(f'Destination: {dst_address}')        #string formating from %s
    
    if ip_proto == 6:
        tcp_udp = "TCP"
    elif ip_proto == 17:
        tcp_proto = "UDP"
    else:
        tcp_udp = "OTHER"
        
    return data, tcp_udp
        
def analyze_ether_header(data_recv):
    '''
    The '!6s6sH' is designed to allow the struct.unpack function to convert the data recievd from the data_recv
    variable which comes in a long string of data and needs to be broken down to be interpreted
    and integrated for usage!
    '''
    
    ip_bool = False
    
    eth_hdr = struct.unpack('!6s6sH', data_recv[:14])
    dest_mac = binascii.hexlify(eth_hdr[0])
    src_mac = binascii.hexlify(eth_hdr[1])
    proto = eth_hdr[2] >> 8
    data = data_recv[:14]
    
    print('__________ETHERNET HEADER_________')
    print(f'Destination MAC: {dest_mac[0:2]}, {dest_mac[2:4]}, {dest_mac[4:6]}, {dest_mac[6:8]}, {dest_mac[8:10]}, {dest_mac[10:12]}')
    print(f'Source MAC: {src_mac[0:2]}, {src_mac[2:4]}, {src_mac[4:6]}, {src_mac[6:8]}, {src_mac[8:10]}, {src_mac[10:12]}')
    print(f'PROTOCOL: {proto}')

    if proto == 0x08:
        ip_bool = True
        
    return data, ip_bool    
    
def main():
    global sock_created
    global sniffer_socket
    
    if sock_created == False:
        #sniffer_socket=socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
        sniffer_socket =socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.htons(0x0003))
        sock_created = True
        
    data_recv = sniffer_socket.recv(2048)
    os.system('clear')
    
    data_recv, ip_bool = analyze_ether_header(data_recv)
    if ip_bool:
        data_recv, tcp_udp = analyze_ip_header(data_recv)
    else:
        return
    
    if tcp_udp == "TCP":
        data_recv = analyze_tcp_header(data_recv)
    elif tcp_udp == "UDP":
        data_recv = analyze_udp_header(data_recv)
    else:
        return
    
while True:
    main()
    