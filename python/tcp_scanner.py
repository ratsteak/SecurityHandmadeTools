import sys
import traceback
import socket

def knocking_port(ip,port):
    tcp(ip,port)

def tcp(ip,port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(0.5)
    con = s.connect_ex((ip,port))
    if con == 0:
        print("TCP "+str(port))
    s.close

try:
    for cont in range(1,int(sys.argv[1])):
        knocking_port(sys.argv[2],cont)
except:
    traceback.print_exc()
    print("USAGE python tcp_scanner.py MAXPORT IP")




