
import unittest
from src.tateti import Tateti
from src.tablero import PosOcupadaException, PosicionInvalidaException

class TestTateti(unittest.TestCase):
    def test_estado_inicial(self):
       
        juego = Tateti()
        
        self.assertEqual(juego.turno, "X")   
        self.assertFalse(juego.juego_terminado)

    def test_cambia_turno_luego_de_una_jugada(self):
        juego = Tateti()
        
        juego.ocupar_una_de_las_casillas(0, 0)  
        
        self.assertEqual(juego.turno, "O")  

    def test_levanta_posicion_invalida(self):
        juego = Tateti()
        with self.assertRaises(PosicionInvalidaException):
            juego.ocupar_una_de_las_casillas(-1, 0)

    def test_levanta_posicion_ocupada(self):
        juego = Tateti()
        juego.ocupar_una_de_las_casillas(0, 0) 
        with self.assertRaises(PosOcupadaException):
            juego.ocupar_una_de_las_casillas(0, 0)

    def test_gana_x_en_fila(self):
        juego = Tateti()
        juego.ocupar_una_de_las_casillas(0, 0)  # X
        juego.ocupar_una_de_las_casillas(1, 0)  # O
        juego.ocupar_una_de_las_casillas(0, 1)  # X
        juego.ocupar_una_de_las_casillas(1, 1)  # O
        juego.ocupar_una_de_las_casillas(0, 2)  # X gana
        # verifico
        self.assertTrue(juego.juego_terminado)
        self.assertEqual(juego.ganador, "X")

    def test_empate_sin_ganador(self):
        juego = Tateti()
        # Lleno el tablero sin 3 en línea
        # X O X
        # X O O
        # O X X
        juego.ocupar_una_de_las_casillas(0, 0)  # X
        juego.ocupar_una_de_las_casillas(0, 1)  # O
        juego.ocupar_una_de_las_casillas(0, 2)  # X
        juego.ocupar_una_de_las_casillas(1, 1)  # O
        juego.ocupar_una_de_las_casillas(1, 0)  # X
        juego.ocupar_una_de_las_casillas(1, 2)  # O
        juego.ocupar_una_de_las_casillas(2, 1)  # X
        juego.ocupar_una_de_las_casillas(2, 0)  # O
        juego.ocupar_una_de_las_casillas(2, 2)  # X
        # verifico
        self.assertTrue(juego.juego_terminado)
        self.assertIsNone(juego.ganador)

    def test_no_permite_jugar_despues_de_terminado(self):
        juego = Tateti()
        # Hago que termine rápido (gana X fila 0)
        juego.ocupar_una_de_las_casillas(0, 0)  # X
        juego.ocupar_una_de_las_casillas(1, 0)  # O
        juego.ocupar_una_de_las_casillas(0, 1)  # X
        juego.ocupar_una_de_las_casillas(1, 1)  # O
        juego.ocupar_una_de_las_casillas(0, 2)  # X gana, termina
        # intento otra jugada -> debería fallar
        with self.assertRaises(Exception):
            juego.ocupar_una_de_las_casillas(2, 2)

    def test_turno_vuelve_a_x_luego_de_dos(self):
        g = Tateti()
        g.ocupar_una_de_las_casillas(0, 0)  # X
        g.ocupar_una_de_las_casillas(1, 1)  # O
        self.assertEqual(g.turno, "X")

    def test_empieza_con_tablero_vacio(self):
        g = Tateti()
        vacias = sum(1 for fila in g.tablero.contenedor for c in fila if c == "")
        self.assertEqual(vacias, 9)

    def test_gana_o_en_columna(self):
        g = Tateti()
        g.ocupar_una_de_las_casillas(0, 1)  # X
        g.ocupar_una_de_las_casillas(0, 0)  # O
        g.ocupar_una_de_las_casillas(1, 1)  # X
        g.ocupar_una_de_las_casillas(1, 0)  # O
        g.ocupar_una_de_las_casillas(2, 2)  # X
        g.ocupar_una_de_las_casillas(2, 0)  # O gana
        self.assertTrue(g.juego_terminado)
        self.assertEqual(g.ganador, "O")

if __name__ == "__main__":
    unittest.main()
