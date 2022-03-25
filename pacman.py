import random
from tablero import Tablero
from usuario import Usuario

# tablero
global objTablero
jugadores = []


def inicio():
    print('=== Menu de inicio ===')
    print('1. Iniciar Juego')
    print('2. Salir')
    try:
        resp = int(input('\nSelecciona una opcion : '))

        if (resp == 1):
            infoUsuario()
        elif(resp == 2):
            exit()
        else:
            raise ValueError("Fuera del rango")
    except ValueError:
        print('\nValor incorrecto\n')
        inicio()


# def usuario():


def infoUsuario():
    try:
        nombre = str(input("Nombre de usuario : "))
        global jugador
        jugador = Usuario(nombre)
        jugadores.append(jugador)
        dimensiones()
    except ValueError:
        infoUsuario()


def dimensiones():
    global objTablero
    objTablero = Tablero(jugador)
    print("=== Generando tablero y posicion inicial ===")
    print("Tablero")

    cantidadPremios()


def cantidadPremios():
    try:
        cantidad = random.randint(3, 6)
        if(cantidad > 0 and cantidad < 13):
            objTablero.setPremios(cantidad)
            cantidadParedes()
        else:
            raise ValueError("Fuera del rango")

    except ValueError:
        # print('\nValor incorrecto\n')
        cantidadPremios()


def cantidadParedes():
    try:
        cantidad = random.randint(5, 12)
        if(cantidad > 0 and cantidad < 7):
            objTablero.setParedes(cantidad)
            cantidadFantasmas()
        else:
            raise ValueError("Fuera del rango")

    except ValueError:
        # print('\nValor incorrecto\n')
        cantidadPremios()


def cantidadFantasmas():
    try:
        cantidad = random.randint(1, 6)
        if(cantidad > 0 and cantidad < 7):
            objTablero.setFantasmas(cantidad)
            estadoInicial()
        else:
            raise ValueError("Fuera del rango")

    except ValueError:
        # print('\nValor incorrecto\n')
        cantidadPremios()


def estadoInicial():
    objTablero.generarEstadoInicial()
    objTablero.mostrarTablero()
    posicionInicial()


def posicionInicial():
    try:
        fil = random.randint(1, 5)
        col = random.randint(1, 6)

        objTablero.posicionInicialPacman(fil-1, col-1)

        juego()

    except ValueError:
        # print("Valor incorrecto")
        posicionInicial()
    except Exception:
        # print("Posicion invalida")
        posicionInicial()


def juego():
    while(not objTablero.juegoTerminado):
        objTablero.mostrarTablero()
        print("W: Arriba | S: Abajo | D: Derecha | A: Izquierda | F: finalizar Partida")
        try:
            tecla = str(input()).upper()
            if(tecla == 'W' or tecla == 'S' or tecla == 'D' or tecla == 'A' or tecla == 'F'):
                mensaje = objTablero.movimiento(tecla)
                print(mensaje)
            else:
                raise ValueError("Tecla invalida")

        except ValueError:
            print("valor invalido")

    print(" Juego Finalizado ")
    inicio()


inicio()
