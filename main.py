import numpy as np
import random

class casilla:
    mina = ''
    bandera = ''
    pisada = ''
    numero = ''

    def __init__(self, m, b, p, n):
        self.mina = m
        self.bandera = b
        self.pisada = p
        self.numero = n

    def mostrar(self):
        print (self.mina, self.bandera, self.pisada, self.numero)

def mostrarTablero (arreglo):
    for a in range(5):
        for b in range(5):
            if arreglo[a][b].pisada == 1:
                if arreglo[a][b].mina == 1:
                    print ("☒", end = " ")
                elif arreglo[a][b].numero > 0:
                    print (arreglo[a][b].numero, end = " ")
                else:
                    print ("▣", end = " ")
            else:
                if arreglo[a][b].bandera == 1:
                    print ("☑", end = " ")
                else:
                    print ("▢", end = " ")
        print()

def establecerNumMinas(arreglo):
    for a in range(5):
        for b in range(5):
            if b == 0:
                if a < 4:
                    if arreglo[a+1][b+1].mina == 1:
                        arreglo[a][b].numero += 1

                    if arreglo[a+1][b].mina == 1:
                        arreglo[a][b].numero += 1
                if a > 0:
                    if arreglo[a-1][b].mina == 1:
                        arreglo[a][b].numero += 1

                    if arreglo[a-1][b+1].mina == 1:
                        arreglo[a][b].numero += 1
                if arreglo[a][b+1].mina == 1:
                    arreglo[a][b].numero += 1
            elif a == 0:
                if b < 4:
                    if arreglo[a][b+1].mina == 1:
                        arreglo[a][b].numero += 1

                    if arreglo[a+1][b+1].mina == 1:
                        arreglo[a][b].numero += 1
                if b > 0:
                    if arreglo[a][b-1].mina == 1:
                        arreglo[a][b].numero += 1

                    if arreglo[a+1][b-1].mina == 1:
                        arreglo[a][b].numero += 1
                if arreglo[a+1][b].mina == 1:
                    arreglo[a][b].numero += 1
            else:
                try:
                    if arreglo[a][b+1].mina == 1:
                        arreglo[a][b].numero += 1
                except IndexError:
                    None
                try:
                    if arreglo[a+1][b+1].mina == 1:
                        arreglo[a][b].numero += 1
                except IndexError:
                    None
                try:
                    if arreglo[a+1][b].mina == 1:
                        arreglo[a][b].numero += 1
                except IndexError:
                    None
                try:
                    if arreglo[a+1][b-1].mina == 1:
                        arreglo[a][b].numero += 1
                except IndexError:
                    None
                try:
                    if arreglo[a][b-1].mina == 1:
                        arreglo[a][b].numero += 1
                except IndexError:
                    None
                try:
                    if arreglo[a-1][b-1].mina == 1:
                        arreglo[a][b].numero += 1
                except IndexError:
                    None
                try:
                    if arreglo[a-1][b].mina == 1:
                        arreglo[a][b].numero += 1
                except IndexError:
                    None
                try:
                    if arreglo[a-1][b+1].mina == 1:
                        arreglo[a][b].numero += 1
                except IndexError:
                    None

def pisarCasillasAlrededor(arreglo, a, b):
    if b == 0:
        if a < 4:
            arreglo[a+1][b+1].pisada = 1
            arreglo[a+1][b].pisada = 1
        if a > 0:
            arreglo[a-1][b].pisada = 1
            arreglo[a-1][b+1].pisada = 1
        arreglo[a][b+1].pisada = 1
    elif a == 0:
        if b < 4:
            arreglo[a][b+1].pisada = 1

            arreglo[a+1][b+1].pisada = 1
        if b > 0:
            arreglo[a][b-1].pisada = 1

            arreglo[a+1][b-1].pisada = 1
        arreglo[a+1][b].pisada = 1
    else:
        try:
            arreglo[a][b+1].pisada = 1
        except IndexError:
            pass
        try:
            arreglo[a+1][b+1].pisada = 1
        except IndexError:
            pass
        try:
            arreglo[a+1][b].pisada = 1
        except IndexError:
            pass
        try:
            arreglo[a+1][b-1].pisada = 1
        except IndexError:
            pass
        try:
            arreglo[a][b-1].pisada = 1
        except IndexError:
            pass
        try:
            arreglo[a-1][b-1].pisada = 1
        except IndexError:
            pass
        try:
            arreglo[a-1][b].pisada = 1
        except IndexError:
            pass
        try:
            arreglo[a-1][b+1].pisada = 1
        except IndexError:
            pass
    
def pisarCasilla (arreglo):
    for a in range(5):
        for b in range(5):
            if arreglo[a][b].numero == 0 and arreglo[a][b].pisada == 1 and arreglo[a][b].mina == 0:
                pisarCasillasAlrededor(arreglo, a, b)
    arreglo = arreglo [::-1]
    for a in range(5):
        for b in range(5):
            if arreglo[a][b].numero == 0 and arreglo[a][b].pisada == 1 and arreglo[a][b].mina == 0:
                pisarCasillasAlrededor(arreglo, a, b)

def ingresarCasilla (a, b):
    a = int (input("Ingrese el numero de la fila: "))
    b = int (input("Ingrese el numero de la columna: "))
    a -= 1
    b -= 1
    a = np.clip (a, 0, 4)
    b = np.clip (b, 0, 4)
    return a, b

def pisarMinas (arreglo):
    for a in range(5):
        for b in range(5):
            if arreglo[a][b].mina == 1:
                arreglo[a][b].pisada = 1

def comprobarMina (arreglo):
    a = 0
    b = 0
    explosion = 0
    a, b = ingresarCasilla (a, b)
    if arreglo[a][b].mina == 0:
        arreglo[a][b].pisada = 1
        pisarCasilla (arreglo)
    else:
        print("💥")
        pisarMinas (arreglo)
        explosion = 1
        mostrarTablero(arreglo)
    return explosion

def ponerBandera (arreglo):
    a = 0
    b = 0
    a, b = ingresarCasilla (a, b)
    if arreglo[a][b].bandera == 0 and arreglo[a][b].pisada == 0:
        arreglo[a][b].bandera = 1
    else:
        arreglo[a][b].bandera = 0

def comprobarVictoria (arreglo):
    contadorMinas = 0
    contadorBanderas = 0
    victoria = 0
    for a in range(5):
        for b in range(5):
            if arreglo[a][b].mina == 1:
                contadorMinas += 1
    for a in range(5):
        for b in range(5):
            if arreglo[a][b].mina == 1 and arreglo[a][b].bandera == 1:
                contadorBanderas += 1
    if contadorBanderas == contadorMinas:
        victoria = 1
        pisarMinas(arreglo)
    return victoria

def cargarMinas (arreglo):
    contador = 0
    mina = 0
    for a in range(5):
        for b in range(5):
            if contador < 4:
                mina = random.randint(0,4)
                if mina == 1:
                    arreglo[a][b].mina = mina
                    contador += 1
    if contador < 4:
        arreglo = arreglo [::-1]
        for a in range(5):
            for b in range(5):
                if contador < 4:
                    mina = random.randint(0,4)
                    if mina == 1:
                        arreglo[a][b].mina = mina
                        contador += 1

def iniciarJuego (arreglo):
    opcion = 0
    derrota = 0
    victoria = 0

    cargarMinas(arreglo)

    establecerNumMinas(arreglo)

    while derrota == 0 and victoria == 0:
        mostrarTablero(arreglo)

        opcion = int(input("Elija su movimiento: \n1. Pisar casilla\n2. Colocar o quitar bandera\n"))

        #opcion = np.clip (opcion, 1, 2)
        
        if opcion == 1:
            derrota = comprobarMina(arreglo)
        else:
            ponerBandera(arreglo)
        
        if derrota == 1:
            break

        pisarCasilla(arreglo)

        victoria = comprobarVictoria(arreglo)

        if victoria == 1:
            print ("¡Victoria! Has descubierto todas las minas.")
            mostrarTablero(arreglo)
            break

c1 = casilla(0,0,0,0)
c2 = casilla(0,0,0,0)
c3 = casilla(0,0,0,0)
c4 = casilla(0,0,0,0)
e1 = casilla(0,0,0,0)

c5 = casilla(0,0,0,0)
c6 = casilla(0,0,0,0)
c7 = casilla(0,0,0,0)
c8 = casilla(0,0,0,0)
e2 = casilla(0,0,0,0)

c9 = casilla(0,0,0,0)
c10 = casilla(0,0,0,0)
c11 = casilla(0,0,0,0)
c12 = casilla(0,0,0,0)
e3 = casilla(0,0,0,0)

c13 = casilla(0,0,0,0)
c14 = casilla(0,0,0,0)
c15 = casilla(0,0,0,0)
c16 = casilla(0,0,0,0)
e4 = casilla(0,0,0,0)

e5 = casilla(0,0,0,0)
e6 = casilla(0,0,0,0)
e7 = casilla(0,0,0,0)
e8 = casilla(0,0,0,0)
e9 = casilla(0,0,0,0)

tablero = [[c1, c2, c3, c4, e1], [c5, c6, c7, c8, e2], [c9, c10, c11, c12, e3], [c13, c14, c15, c16,e4], [e5,e6,e7,e8,e9]]

iniciarJuego(tablero)