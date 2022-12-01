#importando librerias

import sys
from socket import *

#MODO DE EJECUCION DEL SCRIPT
host = sys.argv[1]
portstrs = sys.argv[2].split('-')

start_port = int(portstrs[0])
end_port = int(portstrs[1])

target_ip = gethostbyname(host)
open_ports = []

for port in range(start_port, end_port):
    #print("escaneando: " + str(port))
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        open_ports.append(port)

print("open_ports:")

for i in open_ports:
    print(i)