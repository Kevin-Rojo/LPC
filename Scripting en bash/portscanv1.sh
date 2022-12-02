#!/bin/bash
#
#Escaner de puertos usando archivo /dev

direccion_ip=$1
puertos="20,21,22,23,25,50,51,53,80,110,119,135,137,139,143,161,389,1025,1443,3389,443,8080,10000"

[ $# -eq 0 ] && {echo "Modo de uso $0 192.198.1.1"; exit 1; }


IFS=,
for port in $puertos
do
    timeout 1 bash -c "echo > /dev/tcp/$direccion_ip/$port > /dev/null 2>&1" &&\
    echo $direccion_ip":"$port" is open"\
    ||\
    echo $direccion_ip":"$port" is closed"\
done