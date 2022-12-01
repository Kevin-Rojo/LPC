#Kevin Samuel Rojo Ortega
#1723337

#importando librerias
import sys
import threading
from socket import *

def tcp_test(port, target_ip):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        print("opened Port: ", port)


if __name__=='__main__':
    host = sys.argv[1]
    portstr = sys.argv[2].split('-')
    start_port =  int(portstr[0])
    end_port = int(portstr[1])

    target_ip = gethostbyname(host)

    hilos = []
    for port in range(start_port, end_port):
        hilo = threading.Thread(target=tcp_test, args=(port, target_ip))
        hilos.append(hilo)
        hilo.start()