import unittest
from src.tablero import Tablero, PosOcupadaException, PosicionInvalidaException

class TestTablero(unittest.TestCase):

    def setUp(self):
        self.tablero = Tablero()

    def test_poner_ficha_valida(self):
        self.tablero.poner_la_ficha(0, 0, 'X')
        self.assertEqual(self.tablero.contenedor[0][0], 'X')

    def test_posicion_ocupada(self):
        self.tablero.poner_la_ficha(1, 1, 'O')
        with self.assertRaises(PosOcupadaException):
            self.tablero.poner_la_ficha(1, 1, 'X')

    def test_posicion_fuera_rango(self):
        with self.assertRaises(PosicionInvalidaException):
            self.tablero.poner_la_ficha(-1, 0, 'X')

    def test_ganador_fila(self):
        self.tablero.poner_la_ficha(0, 0, 'X')
        self.tablero.poner_la_ficha(0, 1, 'X')
        self.tablero.poner_la_ficha(0, 2, 'X')
        self.assertEqual(self.tablero.verificar_ganador(), 'X')

    def test_ganador_columna(self):
        self.tablero.poner_la_ficha(0, 1, 'O')
        self.tablero.poner_la_ficha(1, 1, 'O')
        self.tablero.poner_la_ficha(2, 1, 'O')
        self.assertEqual(self.tablero.verificar_ganador(), 'O')

    def test_ganador_diagonal(self):
        self.tablero.poner_la_ficha(0, 0, 'X')
        self.tablero.poner_la_ficha(1, 1, 'X')
        self.tablero.poner_la_ficha(2, 2, 'X')
        self.assertEqual(self.tablero.verificar_ganador(), 'X')

    def test_tablero_lleno_true(self):
        jugadas = [
            ('X', 0, 0), ('O', 0, 1), ('X', 0, 2),
            ('X', 1, 0), ('O', 1, 1), ('X', 1, 2),
            ('O', 2, 0), ('X', 2, 1), ('O', 2, 2)
        ]
        for ficha, fil, col in jugadas:
            self.tablero.poner_la_ficha(fil, col, ficha)
        self.assertTrue(self.tablero.tablero_lleno())

    def test_poner_o(self):
        t = Tablero()
        t.poner_la_ficha(2, 1, "O")
        self.assertEqual(t.contenedor[2][1], "O")

    def test_ganador_columna_0(self):
        t = Tablero()
        t.poner_la_ficha(0, 0, "X")
        t.poner_la_ficha(1, 0, "X")
        t.poner_la_ficha(2, 0, "X")
        self.assertEqual(t.verificar_ganador(), "X")


    def test_posicion_invalida_borde(self):
        t = Tablero()
        with self.assertRaises(PosicionInvalidaException):
            t.poner_la_ficha(0, 3, "X")
if __name__ == '__main__':
    unittest.main()