class PosOcupadaException(Exception):
    pass

class PosicionInvalidaException(Exception):
    pass

class Tablero:
    def __init__(self):
        self.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]

    def poner_la_ficha(self, fil, col, ficha):
        # verificar que la posición este dentro del rango 
        if fil < 0 or fil > 2 or col < 0 or col > 2:
            raise PosicionInvalidaException("Posición fuera del tablero. ")
        
        # verificar si esta ocupado
        if self.contenedor[fil][col] == "":
            self.contenedor[fil][col] = ficha
        else:
            raise PosOcupadaException("Posición ocupada.")

    def mostrar_tablero(self):
        print("  0 1 2")
        for i, fila in enumerate(self.contenedor):
            fila_mostrar = []
            for celda in fila:
                if celda != "":
                    fila_mostrar.append(celda)
                else:
                    fila_mostrar.append("_")
            print(f"{i} {' '.join(fila_mostrar)}")

    def verificar_ganador(self):
        # verificar filas
        for fila in self.contenedor:
            if fila[0] == fila[1] == fila[2] != "":
                return fila[0]
        
        # verificar columnas
        for col in range(3):
            if self.contenedor[0][col] == self.contenedor[1][col] == self.contenedor[2][col] != "":
                return self.contenedor[0][col]
        
        # verificar diagonales
        if self.contenedor[0][0] == self.contenedor[1][1] == self.contenedor[2][2] != "":
            return self.contenedor[0][0]
        if self.contenedor[0][2] == self.contenedor[1][1] == self.contenedor[2][0] != "":
            return self.contenedor[0][2]
        
        return None

    def tablero_lleno(self):
        for fila in self.contenedor:
            if "" in fila:
                return False
        return True