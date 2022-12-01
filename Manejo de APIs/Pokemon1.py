import requests

# Kevin Samuel Rojo Ortega
#
# 1723337

def menu () -> bool:
    print("1. Consultar pokemon-form")
    print("2. Consultar por Tipo")
    print("3. Salir")
    print("---------------------------------------------------")
    try:
        n_opcion = int(input("Ingrese una opcion: "))
        if  n_opcion == 1 or n_opcion == 2:
            opcion=True
            return opcion, n_opcion
        elif n_opcion == 3:
            opcion=False
            return opcion, n_opcion

    except: 
        print("Selecciona solo numeros")
        opcion = True
        return opcion,n_opcion

def repetir_menu() -> bool:

    print("1. Repetir menu:")
    print("2. Salir")
    try:
        n_opcion = int(input("Ingrese una opcion: "))
        print("---------------------------------------------------")
        if  n_opcion == 1:
            opcion=True
            validate = False
            return opcion, validate
        elif n_opcion == 2:
            opcion=False
            validate = False
            return opcion, validate

    except:
        print("--------------------------")
        print("Selecciona solo numeros")
        opcion = True
        validate = True
        return opcion, validate


if __name__=="__main__":
    opcion= True
    while opcion:
        opcion, n_opcion = menu()
        
        # LA OPCION 1 ES LA PARTE DEL LA ACTVIDAD
        if n_opcion == 1:
            
            url = "https://pokeapi.co/api/v2/pokemon-form/"

            response = requests.get(url)
            
            if response.status_code == 200 :
                payload = response.json()
                results = payload.get('results',[])
                if results:
                    for pokemon in results:
                        name = pokemon['name']
                        print(name)
                print("---------------------------------------------------")

        # LA OPCION 2 ME TOME LA LIBERTAD DE HACER OTRA PETICION DIFERENTE LEYENDO LA DOCUMENTACION
        elif n_opcion == 2:

            tipo = input("Ingrese el tipo de pokemon: ")
            url = "https://pokeapi.co/api/v2/type/" + tipo + "/"

            response = requests.get(url)
            
            if response.status_code == 200 :
                payload = response.json()
                results = payload.get('pokemon',[])
                print()
                if results:
                    for pokemon in results:
                        name = pokemon['pokemon']['name']
                        print(name)
                print("---------------------------------------------------")

        validate  = True
        if n_opcion == False:
            validate = False
        while validate:
            opcion,validate = repetir_menu()
            
        