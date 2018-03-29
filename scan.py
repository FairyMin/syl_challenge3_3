#coding:utf-8

import socket
import getopt
import sys

def scan():
    ip = '127.0.0.1'
    port = 3306
    test_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result = test_sock.connect_ex((ip,port))
    if result == 0:
        print("Port is open")
    else:
        print("Port is closed")


if __name__=='__main__':
    scan()
