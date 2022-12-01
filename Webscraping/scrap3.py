#Importar Modulos
import requests
from bs4 import BeautifulSoup as bs

#Obtener Informacion HTML de la URL
url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)

# Analizamos el Contenido con BeautifullSoup
soup = bs(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

# Buscar todos los elementos que el class "card-content"
job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    print(job_element)