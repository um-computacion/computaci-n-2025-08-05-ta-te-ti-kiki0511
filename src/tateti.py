from src.tablero import Tablero, PosOcupadaException, PosicionInvalidaException

class Tateti:
    def __init__(self):
        self.turno = "X"
        self.tablero = Tablero()
        self.ganador = None
        self.juego_terminado = False

    def ocupar_una_de_las_casillas(self, fil, col):
        if self.juego_terminado:
            raise Exception("El juego ya terminó!")
        
        # poner la ficha
        self.tablero.poner_la_ficha(fil, col, self.turno)
        
        # verificar si hay ganador
        self.ganador = self.tablero.verificar_ganador()
        if self.ganador:
            self.juego_terminado = True
            return
        
        # verificar si es empate
        if self.tablero.tablero_lleno():
            self.juego_terminado = True
            return
        
        # cambia turno. va suceder solo si se pudo poner la ficha
        if self.turno == "X":
            self.turno = "O"  
        else:
            self.turno = "X"