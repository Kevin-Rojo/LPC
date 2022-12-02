#!/bin/sh
#Kevin Samuel Rojo Ortega
#1723337

log(){
        MESSAGE=${@:-""}
        echo "${MESSAGE}"
}

logWarning(){

	START='\033[01;33m'
	END='\033[00;00m'
	MESSAGE=${@:-""}
	echo "${START}${MESSAGE}${END}"
}

net_scan(){
    log "formato ###.###.###.###/##: "
    read -p 'Subred a Escanear: ' subnet
    nmap -sn $subnet > RED_SCAN.txt
}

ip_scan(){
    log "formato ###.###.###.###"
    read -p 'Direccion IP a Escanear: ' ip
    nmap -v -A $ip > IP_SCAN.txt
}

udp_scan(){
    log "formato ###.###.###.###"
    read -p 'Direccion IP a Escanear: ' ip
    nmap -sU $ip --top-ports 100 -vv > UDP_SCAN.txt
}

script_scan(){
    log "formato ###.###.###.###"
    read -p 'Direccion IP a Escanear: ' ip
    read -p 'Script a Utilizar: ' script
    nmap --script $script $ip > SCRIPT_SCAN.txt
}


while true; do
    log "Menu"
    log "1. Escaneo de RED"
    log "2. Escaneo Individual"
    log "3. Escaneo UDP"
    log "4. Escaneo de Script"
    log "5. Salir"
    read -p "Seleccione una opcion de 1 a 5: " op
    case $op in
        [1]* ) net_scan; log "Escaneo Terminado";;
        [2]* ) ip_scan; log "Escaneo Terminado";;
        [3]* ) udp_scan; log "Escaneo Terminado";;
        [4]* ) script_scan; log "Escaneo Terminado";;
        [5]* ) log "Saliendo del Programa";exit;;        
        * ) logWarning "Seleccione una Opción de 1 a 5.";;
    esac
done