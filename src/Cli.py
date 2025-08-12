from src.tateti import Tateti


def main():
    print(" Bienvenidos al Tateti! ")

    juego = Tateti()
    while not juego.juego_terminado:
        print("=========================")
        print("Tablero actual:")
        juego.tablero.mostrar_tablero()
        turno_actual = juego.turno
        print("Turno del jugador: " + turno_actual)
        try:
            fil = int(input("Ingrese fila (0-2): "))
            col = int(input("Ingrese columna (0-2): "))
            juego.ocupar_una_de_las_casillas(fil, col)
        except ValueError:
            print("Error: debe ingresar números enteros")
            continue
        except Exception as e:
            print("Error: " + str(e))
            continue
    
    # mostrar resultado final
    print("\n" + "=========================")
    print("JUEGO TERMINADO")
    juego.tablero.mostrar_tablero()
    
    if juego.ganador:
        print("ganó el jugador " + juego.ganador + " !")
    else:
        print("empate, intente nuevamente ")

if __name__ == '__main__':
    main()