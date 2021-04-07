import os
from random import randrange

DIM = 3
WIN = 3
X_FICHA = "X"
O_FICHA = "O"
LIBRE = " "

def iniciar_tablero():
    tablero = []
    for i in range(DIM):
        fila = []
        for j in range(DIM):
            fila.append(LIBRE)
        tablero.append(fila)
    return tablero

def mostrar_linea():
    print("+", end='')
    for i in range(DIM*2 -1):
        if i % 2 == 1:
            print("+", end = '')
        else:
            print("-", end='')
    print("+")

def mostrar_tablero(tablero):
    mostrar_linea()
    for fila in tablero:
        print("|",end='')
        for casilla in fila:
            print("{}|".format(casilla), end='')
        print("")
        mostrar_linea()
    print("")

def mostrar_puntuacion(marcador, jugador1, jugador2):
    print("+--------------+-", end='')
    for _ in range(len(jugador1)+6+len(jugador2)+4):
        print("-",end='')
    print("+")

    print("|VICTORIAS --> | ", end = '')
    print("{}: {} | ".format(jugador1, marcador[0]), end = '')
    print("{}: {} |".format(jugador2, marcador[1]))

    print("+--------------+-", end='')
    for _ in range(len(jugador1)+6+len(jugador2)+4):
        print("-",end='')
    print("+")

    print("")


def mostrar_bienvenida():
    os.system("clear")
    with open("banner.txt",'r') as f:
        print(f.read())
    
    print("\nBy Alburrito\t https://github.com/Alburrito\n\n")

def comprobar_victoria(tablero, ficha_turno):
    if comprobar_filas(tablero, ficha_turno):
        return True
    if comprobar_columnas(tablero, ficha_turno):
        return True
    if comprobar_diagonales(tablero, ficha_turno):
        return True

    return False

def comprobar_filas(tablero, ficha_turno):
    for fila in tablero:
        contador = 0
        for casilla in fila:
            if casilla == ficha_turno:
                contador += 1
            else:
                contador = 0
            if contador == WIN:
                return True
    return False

def comprobar_columnas(tablero, ficha_turno):
    for columna in range(DIM):
        contador = 0
        for fila in range(DIM):
            if tablero[fila][columna] == ficha_turno:
                contador += 1
            else:
                contador = 0
            if contador == WIN:
                return True
    return False

def comprobar_diagonales(tablero, ficha_turno):
    contador = 0
    for i in range(DIM):
        if tablero[i][i] == ficha_turno:
            contador += 1
        else:
            contador = 0
        if contador == WIN:
            return True

    columna = DIM-1
    contador = 0
    for fila in range(DIM):
        if tablero[fila][columna] == ficha_turno:
            contador += 1
        else:
            contador = 0
        columna -= 1
        if contador == WIN:
            return True
    
    return False
    
def jugar_ficha_turno(tablero, turno):
    
    fila = int(input("Introduce la fila [1-{}]: ".format(DIM)))
    while fila < 1 or fila > 3:
        print("La opción debe estar comprendida entre 1 y {}".format(DIM))
        fila = int(input("Introduce la fila [1-{}]: ".format(DIM)))
    fila -= 1

    columna = int(input("Introduce la columna [1-{}]: ".format(DIM)))
    while columna < 1 or columna > 3:
        print("La opción debe estar comprendida entre 1 y {}".format(DIM))
        columna = int(input("Introduce la columna [1-{}]: ".format(DIM)))
    columna -= 1

    while tablero[fila][columna] != LIBRE:
        print("ERROR: Debes escoger una casilla libre")
        fila = int(input("Introduce la fila [1-{}]: ".format(DIM)))
        while fila < 1 or fila > 3:
            print("La opción debe estar comprendida entre 1 y {}".format(DIM))
            fila = int(input("Introduce la fila [1-{}]: ".format(DIM)))
        fila -= 1

        columna = int(input("Introduce la columna [1-{}]: ".format(DIM)))
        while columna < 1 or columna > 3:
            print("La opción debe estar comprendida entre 1 y {}".format(DIM))
            columna = int(input("Introduce la columna [1-{}]: ".format(DIM)))
        columna -= 1

    if turno == 1:
        tablero[fila][columna] = X_FICHA
        return 2
    else:
        tablero[fila][columna] = O_FICHA
        return 1

    return False


def main():
    fin_juego = False
    mostrar_bienvenida()
    jugador1 = input("Introduce nombre del jugador 1 ({}): ".format(X_FICHA))
    jugador2 = input("Introduce nombre del jugador 2 ({}): ".format(O_FICHA))
    marcador = [0,0]
    while not fin_juego:
        tablero = iniciar_tablero()
        jugadas = 0
        turno = randrange(1, 3)
        fin = False
        while not fin:
            os.system("clear")

            mostrar_puntuacion(marcador, jugador1, jugador2)
            mostrar_tablero(tablero)

            print("Turno de ", end='')
            if turno == 1:
                print("{}: ({}): ".format(jugador1, X_FICHA))
            else:
                print("{}: ({})): ".format(jugador2, O_FICHA))

            sig_turno = jugar_ficha_turno(tablero, turno)
            jugadas += 1

            if turno == 1 and comprobar_victoria(tablero, X_FICHA):
                os.system("clear")
                marcador[0] += 1
                mostrar_puntuacion(marcador, jugador1, jugador2)
                mostrar_tablero(tablero)
                print("HA GANADO {}!\n---- ENHORABUENA ----".format(jugador1))
                fin = True
            elif turno == 2 and comprobar_victoria(tablero, O_FICHA):
                os.system("clear")
                marcador[1] += 1
                mostrar_puntuacion(marcador, jugador1, jugador2)
                mostrar_tablero(tablero)
                print("HA GANADO {}!\n---- ENHORABUENA ----".format(jugador2))
                fin = True
            elif jugadas == DIM*DIM:
                os.system("clear")
                mostrar_puntuacion(marcador, jugador1, jugador2)
                mostrar_tablero(tablero)
                print("--- HA SIDO UN EMPATE! ---")
                fin = True

            turno = sig_turno

        print("")
        finalizar = input("¿Quereis jugar otra vez? [si/no]: ")
        while finalizar != "si" and finalizar != "no":
            finalizar = input("Por favor, introducid una opcion valida [si/no]: ")
        
        if finalizar == "no":
            fin_juego = True
    
    print("")
    print("HASTA OTRA!")
    print("")
        
if __name__ == "__main__":
    main()