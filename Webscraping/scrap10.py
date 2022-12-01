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

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_jobs_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_element in python_jobs_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(link.text.strip())
    print()