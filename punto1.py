listaCiclistas=[]
i=1
def agregarCiclista():
        nombre = input(f'Digite el nombre: ')
        edad = input(f'Digite la edad: ')
        pais = input(f'Digite el pais: ')
        equipo = input(f'Digite el equipo: ')
        tiempo = int(input(f'Digite el tiempo: '))

        listaCiclistas.append({'nombre: ':nombre, 'edad: ':edad, 'pais: ':pais, 'equipo: ':equipo, 'tiempo: ':tiempo})
        print("")
    

def buscarCiclistaMasRapido():
        tiempoTmp = 0
        for ciclista in listaCiclistas:
            if(ciclista["tiempo: "] > tiempoTmp):
                ciclistaRapido = ciclista["nombre: "]
                tiempoTmp = ciclista["tiempo: "]
                print("")
            else:
                tiempoTmp = tiempoTmp
        
        return "El ciclista mas rapido es: "+ciclistaRapido

while(i != 0):
    print(".:Menu:.")
    print("1. Agregar Ciclista")
    print("2. Ver Resultado")
    i= int(input("Digite la opcion: "))
    if(i == 1):
        agregarCiclista()
    elif(i == 2):
        print(buscarCiclistaMasRapido())
    else:
        print('Digite una opcion valida')