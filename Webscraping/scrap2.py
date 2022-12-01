#Importar Modulos
import requests
from bs4 import BeautifulSoup as bs

#Obtener Informacion HTML de la URL
url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)

# Analizamos el Contenido con BeautifullSoup
soup = bs(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

# Formateamo la salida del objeto results de BeautifullSoup
print(results.prettify())