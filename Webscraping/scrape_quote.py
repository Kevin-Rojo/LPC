# Kevin Samuel Rojo Ortega
# 1723337

#importar modulos
import requests
import csv
from bs4 import BeautifulSoup as bs

# Direccion de la pagina WEB
url = "http://quotes.toscrape.com"

# Ejecucion de Get-requests
response = requests.get(url)

# Analisis Sintetico del archivo
html = bs(response.text, 'html.parser')

# Extraer todas las citas y autores del archivo html
quotes_html = html.find_all('span', class_="text")
authors_html = html.find_all('small', class_="author")

# Crear una lista de las citas
quotes = list()
for quote in quotes_html:
    print(quote.text)
    quotes.append(quote.text)

# Crear una lista de los autores
authors = list()
for author in authors_html:
    authors.append(author.text)

# Combinar las antradas
for t in zip(quotes, authors):
    print(t)

# Guardar las citas en un archivo csv
with open("./citas_1723337.csv", 'w') as csv_file:
    csv_writter = csv.writer(csv_file, dialect='excel')
    csv_writter.writerow(zip(quotes, authors))        