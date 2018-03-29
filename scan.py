#coding:utf-8

import socket
import getopt
import sys


def scan(ip,port):
    test_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    for i in port:
        result = test_sock.connect_ex((ip,int(i)))
        if result == 0:
            print("%s open"%i)
        else:
            print("%s closed"%i)


if __name__=='__main__':
    try:
        opts,args = getopt.getopt(sys.argv[1:],"",["port=","host="])
    except getopt.GetoptError:
        print("Parameter Error")
        sys.exit(2)
    
    for o,a in opts:
        #判断host地址是够符合规则
        if o == "--host":
            ip_l = a.split('.',3)
            if len(ip_l) == 4:
                for i in ip_l:
                    if i.isdigit() is False:
                        print("Parameter Error")
                        sys.exit(2)
                host=a
            else:
                print("Parameter Error")
                sys.exit(2)
        #获取port的列表 
        elif o == "--port":
            try:
                if "-" in a:
                    range_port = a.split("-",1)
                    port = [x for x in range(int(range_port[0]),int(range_port[1]))]
                else:
                    port = [a]
            except:
                print("Parameter Error")
                sys.exit(2)
        else:
            assert False,"Unhandled option"
    scan(host,port)
