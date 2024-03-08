

"""
# Podemos guardar diferentes elementos

lista_qhaceres = ["Sacar el perro", "Lavar los trastes", "Hacer la tarea"]
print(lista_qhaceres)

# Podemos guardar diferentes tipos de datos

listas_mixta = ["Hola", 1, 2.3, True]

# Extraer elementos de una lista

print(lista_qhaceres[0])


# Creando una tabla donde se agreguen listas

tabla = [
    [5, 4],
    [2, 6],
    [8, 1],
    [5, 5]
]

for fila in tabla:
    for columna in fila:
        print(columna)
    


# simulando un juego de cartas llamado 21

import random # importando la libreria random


# EL juego

juego = []

marcador = [0,0]

while True:
    print("Bienvenidos a mi CASINO")
    jugador = random.randint(2, 26)
    dealer = random.randint(2, 26)

    # La partida
    while True:
        print(f"El jugador saco: {jugador}, EL dealer tine: {dealer}")
        masCartas = input("Quiere mas cartas ?: S/N\n")

        if masCartas == "S":
            jugador = jugador + random.randint(1,13)
        else:
            if jugador == dealer:

                print("Gano el dealer")
                juego.append("dealer")
                break
            elif jugador == 21 or (jugador > dealer and jugador < 21) or (jugador <= 21 and dealer > 21):
                
                print("Gano el jugador")
                juego.append("jugador")
                break
            else:
                print("Gano el dealer")
                juego.append("dealer")
                break

    salir = input("Desea terminar el juego? S/N\n")
    if salir == "S":
        print(juego)
        for i in juego:
            if i == "jugador":
                marcador[0] += 1
            else:
                marcador[1] += 1
        print(marcador)

        break
        
    else:
        print("\n"*20)
"""
