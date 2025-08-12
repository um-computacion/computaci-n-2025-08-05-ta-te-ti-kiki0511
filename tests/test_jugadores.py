import unittest
from src.jugador import Jugador

class TestJugador(unittest.TestCase):

    def test_crear_jugador(self):
        jugador = Jugador("Joaco", "X")
        self.assertEqual(jugador.nombre, "Joaco")
        self.assertEqual(jugador.simbolo, "X")

    def test_simbolo_string(self):
        jugador = Jugador("Naza", "O")
        self.assertIsInstance(jugador.simbolo, str)

    def test_nombre_vacio(self):
        j = Jugador("", "X")
        self.assertEqual(j.nombre, "")

    def test_simbolo_o(self):
        j = Jugador("Ana", "O")
        self.assertEqual(j.simbolo, "O")
        
if __name__ == '__main__':
    unittest.main()
