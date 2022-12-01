import requests

# Kevin Samuel Rojo Ortega
#
# 1723337

def get_pokemons(url="http://pokeapi.co/api/v2/pokemon-form/", offset=0):
        args = {'offset': offset} if offset else {}

        #print(args)
        #input("continuar")

        response = requests.get(url, params=args)
        
        if response.status_code == 200:
            payload = response.json()
            results = payload.get('results',[])

            if results:
                for pokemon in results:
                    name = pokemon['name']
                    print(name)

            validate = True
            while validate:
                try:
                    next = input("¿Continuar el listado? [Y/N]").lower()
                    if next == "y" or next =="n":
                        if next =="y":
                            get_pokemons(offset=offset+20)
                            validate = False
                        else:
                            validate = False
                    else:
                        print("Ingrese una opcion valida")
                except:
                    print("Ingrese solo las Opciones marcadas Y=SI , N=NO")

if __name__=="__main__":
    get_pokemons()