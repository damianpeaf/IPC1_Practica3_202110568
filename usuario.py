
class Usuario:
    nombre = ''
    punteo = 0
    vidas = 1

    def __init__(self, nombre):
        self.nombre = nombre

    def aumentarPuntaje(self):
        self.punteo += 10

    def disminuirVidas(self):
        self.vidas -= 1
