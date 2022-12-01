import requests
import json

# Kevin Samuel Rojo Ortega
#
# 1723337

if __name__=='__main__':
    url = "http://httpbin.org/post"
    argumentos = {'nombre':'Kevin', 'matricula':'1723337', 'curso':'Laboratorio de programacion para ciberseguridad'}

    response = requests.post(url, params=argumentos)

    if response.status_code == 200:
        print(response.content)