import nmap
path_nmap = [r"C:\Program Files (x86)\Nmap\nmap.exe", ]
escaner = nmap.PortScanner(nmap_search_path=path_nmap)

escaner.scan('192.168.100.1', '1-1024', '-v -sV')
escaner.command_line()
escaner.all_hosts()
escaner['direccion ip escaneada'].state()
escaner['direccion ip escaneada'].all_protocols()
escaner['direccion ip escaneada']['tcp'].keys()
escaner['direccion ip escaneada'].has_tcp(21)
escaner['direccion ip escaneada'].has_tcp(22)
escaner['dirección ip escaneada']['tcp'][22]
escaner['dirección ip escaneada']['tcp'][22]['product']


def udp_scan():
    escaner.scan('192.168.100.1', '1-1024', '-n -Pn -sU -p-')

def complete_scan():
    escaner.scan('192.168.100.1', '1-1024', '-n -Pn -sU -F')

def so_scan():
    escaner.scan('192.168.100.1', '1-1024', '-sV -O -v')

def ping_scan():
    print("ping Scan")

def menu():
    print("1. Escaneo UDP")
    print("2. Escaneo Completo")
    print("3. Deteccion de S.O.")
    print("4. Escaneo de Red")
    print("5. Salir")
    opcion = int(input("Ingrese una opcion:"))
    return opcion
opcion=True
while(opcion):
    m_opcion = menu()

    if(m_opcion == 1):
        print("opcion" + str(m_opcion))
        udp_scan()
    elif(m_opcion == 2):
        print("opcion" + str(m_opcion))
        complete_scan()
    elif(m_opcion == 3):
        print("opcion" + str(m_opcion))
        so_scan()
    elif(m_opcion == 4):
        print("opcion" + str(m_opcion))
        ping_scan()
    elif(m_opcion == 5):
        print("Salinedo")
        opcion=False