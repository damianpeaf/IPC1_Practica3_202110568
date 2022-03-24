import random
from usuario import Usuario

FILAS = 5
COLUMNAS = 6

# Items
FANTASMA = "@"
PREMIO = "O"
BLOQUE = "X"
PERSONAJE = "<"


class Tablero:
    tablero = []
    cantidadPremios = 1
    cantidadParedes = 1
    cantidadFantasmas = 1
    elementosRegidos = 0
    jugador = None
    juegoTerminado = False

    posxPacman = 0
    poyPacman = 0

    def __init__(self, jugador):
        self.jugador = jugador
        self.inicializarTablero()

    def inicializarTablero(self):
        self.tablero = []
        for i in range(FILAS):
            fil = []
            for j in range(COLUMNAS):
                fil.append(None)

            self.tablero.append(fil)

    def setPremios(self, c):
        self.cantidadPremios = c

    def setParedes(self, c):
        self.cantidadParedes = c

    def setFantasmas(self, c):
        self.cantidadFantasmas = c

    def movimiento(self, tecla):
        msg = ''

        self.tablero[self.posxPacman][self.posyPacman] = None

        posxAntigua = self.posxPacman
        posyAntigua = self.posyPacman

        if(tecla == 'W'):
            self.posxPacman -= 1
        elif(tecla == 'S'):
            self.posxPacman += 1
        elif(tecla == 'A'):
            self.posyPacman -= 1
        elif(tecla == 'D'):
            self.posyPacman += 1
        elif(tecla == 'F'):
            self.juegoTerminado = True
            msg = 'Juego terminado'

        if(self.posxPacman < 0 or self.posxPacman >= FILAS or self.posyPacman < 0 or self.posyPacman >= COLUMNAS):
            self.posxPacman = posxAntigua
            self.posyPacman = posyAntigua
            msg = 'No es posible atravesar los extremos'

        # Fantasma
        if(self.tablero[self.posxPacman][self.posyPacman] == FANTASMA):
            self.tablero[self.posxPacman][self.posyPacman] = PERSONAJE
            self.jugador.disminuirVidas()

        if(self.tablero[self.posxPacman][self.posyPacman] == PREMIO):
            self.jugador.aumentarPuntaje()
            self.elementosRegidos += 1

        if(self.tablero[self.posxPacman][self.posyPacman] == BLOQUE):
            self.posxPacman = posxAntigua
            self.posyPacman = posyAntigua
            msg = 'No es posible atravesar una pared'

        self.tablero[self.posxPacman][self.posyPacman] = PERSONAJE

        if(self.jugador.vidas == 0):
            self.juegoTerminado = True
            msg = 'Moriste'

        if(self.elementosRegidos == self.cantidadPremios):
            self.juegoTerminado = True
            msg = 'Haz ganado'

        return msg

    def posicionInicialPacman(self, x, y):

        if(x > -1 and x < FILAS and y > -1 and y < COLUMNAS):
            if(self.tablero[x][y] == None):
                self.tablero[x][y] = PERSONAJE
                self.posxPacman = x
                self.posyPacman = y
            else:
                raise Exception("Posicion ya ocupada")
        else:
            raise Exception("Fuera de los limites")

    def mostrarTablero(self):
        print("", "Usuario: ", self.jugador.nombre)
        print("Punteo: ", self.jugador.punteo)

        print("\n-------------------")
        for fila in self.tablero:
            cadena = '|'
            for elemento in fila:
                if(elemento == None):
                    cadena += '   '
                else:
                    car = ' ' + elemento + ' '
                    cadena += car
            print(cadena+"|")
        print("-------------------\n")

    def generarEstadoInicial(self):
        self.generarElemento(self.cantidadPremios, PREMIO)
        self.generarElemento(self.cantidadParedes, BLOQUE)
        self.generarElemento(self.cantidadFantasmas, FANTASMA)

    def generarElemento(self, cantidad, simbolo):

        for i in range(cantidad):
            creado = False

            while(not creado):
                posy = random.randint(0, COLUMNAS-1)
                posx = random.randint(0, FILAS-1)

                if(self.tablero[posx][posy] == None):
                    self.tablero[posx][posy] = simbolo
                    creado = True
