#Importar Modulos
import requests

#Obtener Informacion HTML de la URL
url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)

# Mostrar el texto de la peticion GET
print(page.text)