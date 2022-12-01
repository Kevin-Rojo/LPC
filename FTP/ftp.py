# SCRPIT PARA TRANSFERENCIA FTP
from distutils import text_file
from ftplib import FTP


# Estableciendo conexion al servidor FTP
ftp = FTP('192.168.48.128')

# iniciamos sesion dentro del servidor
ftp.login("samuel","1723337")

#nos movemos hacia el direcotrio upload
ftp.cwd('upload')

#Mostramos el listado de los nombre de archivos dentro de la carpeta del upload
ftp.retrlines("NLST")

#agregamos el archivo al servidor

with open("ADVERTENCIA.txt","rb") as file:

    ftp.storbinary("STOR ADVERTENCIA.txt",file)


ftp.quit()