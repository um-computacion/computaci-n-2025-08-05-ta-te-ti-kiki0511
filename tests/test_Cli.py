import unittest
from unittest.mock import patch
from io import StringIO
from src.Cli import main as cli_main

# clase falsa para simular el tablero
class FakeTablero:
    def mostrar_tablero(self):
        print("[tablero]")

# clase falsa para simular el juego
class FakeTateti:
    def __init__(self):
        self.tablero = FakeTablero()
        self.turno = "X"
        self.ganador = None
        self.juego_terminado = True

class TestCli(unittest.TestCase):
    
    def test_juego_termina_rapido(self):
        fake_juego = FakeTateti()
        
        with patch("src.Cli.Tateti", return_value=fake_juego):
            with patch("sys.stdout", new_callable=StringIO) as output:
                cli_main()
                resultado = output.getvalue()
        
        self.assertIn("Bienvenidos al Tateti", resultado)
        self.assertIn("JUEGO TERMINADO", resultado)

    def test_jugador_x_gana(self):
        fake_juego = FakeTateti()
        fake_juego.juego_terminado = False
        fake_juego.turno = "X"
        fake_juego.ganador = None
        
        def hacer_jugada(fil, col):
            fake_juego.juego_terminado = True
            fake_juego.ganador = "X"
        
        fake_juego.ocupar_una_de_las_casillas = hacer_jugada
        
        inputs = ["0", "0"]
        
        with patch("src.Cli.Tateti", return_value=fake_juego):
            with patch("builtins.input", side_effect=inputs):
                with patch("sys.stdout", new_callable=StringIO) as output:
                    cli_main()
                    resultado = output.getvalue()
        
        self.assertIn("Turno del jugador: X", resultado)
        import re
        self.assertIn("ganó el jugador x", resultado.lower())



    def test_error_con_letras(self):
        fake_juego = FakeTateti()
        fake_juego.juego_terminado = False
        
        def hacer_jugada(fil, col):
            fake_juego.juego_terminado = True
        
        fake_juego.ocupar_una_de_las_casillas = hacer_jugada
        
        inputs = ["a", "0", "0"]  # primera entrada es letra, luego números
        
        with patch("src.Cli.Tateti", return_value=fake_juego):
            with patch("builtins.input", side_effect=inputs):
                with patch("sys.stdout", new_callable=StringIO) as output:
                    cli_main()
                    resultado = output.getvalue()
        
        self.assertIn("Error: debe ingresar números enteros", resultado)
        self.assertIn("JUEGO TERMINADO", resultado)

    def test_casilla_ocupada(self):
        fake_juego = FakeTateti()
        fake_juego.juego_terminado = False
        fake_juego.primer_intento = True
        
        def hacer_jugada(fil, col):
            if fake_juego.primer_intento:
                fake_juego.primer_intento = False
                raise Exception("ocupado")
            fake_juego.juego_terminado = True
        
        fake_juego.ocupar_una_de_las_casillas = hacer_jugada
        
        inputs = ["0", "0", "1", "1"]  # primer intento falla, segundo funciona
        
        with patch("src.Cli.Tateti", return_value=fake_juego):
            with patch("builtins.input", side_effect=inputs):
                with patch("sys.stdout", new_callable=StringIO) as output:
                    cli_main()
                    resultado = output.getvalue()
        
        self.assertIn("Error: ocupado", resultado)
        self.assertIn("JUEGO TERMINADO", resultado)
    
if __name__ == "__main__":
    unittest.main()