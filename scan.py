#coding:utf-8

import socket
import getopt
import sys

def scan(ip,port):
    test_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result = test_sock.connect_ex((ip,port))
    if result == 0:
        print("Port is open")
    else:
        print("Port is closed")


if __name__=='__main__':
    try:
        opts,args = getopt.getopt(sys.argv[1:],"",["port=","host="])
    except getopt.GetoptError:
        print("Parameter Error")
        sys.exit(2)
    print(opts)
    print(args)
    #scan(ip,port)
