# TRABAJO PRACTICO "TATETI" 
**Clase:** 5/08/2025
**Alumno:** Tejada Pareja Joaquin

## Reglas del juego

- El tablero es de 3x3. 
- Dos jugadores, jugador 1: **X** y jugador 2: **O**.
- Gana quien logre alinear tres fichas iguales de forma **horizontal, vertical o diagonal**.
- Si se llenan todas las casillas sin ganador, el resultado es **empate**.

## Como ejecutar el juego:

1. Abrí una terminal en la raíz del proyecto.
2. Ejecutá el siguiente comando:

```bash
PYTHONPATH=. python3 src/Cli.py
```

## Como ejecutar los test:
1. Abrí una terminal en la raíz del proyecto.
2. Ejecutá el siguiente comando:

```bash
PYTHONPATH=. python3 -m unittest discover -s tests -p "test_*.py"
```

# Carpeta scr/

- **Cli.py**
Aqui se maneja la interacción con el usuario: mostrar el tablero, pedir jugadas, anunciar resultados.

- **jugador.py**
Contiene la clase Jugador, que guarda datos del jugador: nombre, símbolo.

- **tablero.py**
Contiene la clase Tablero, que guarda y gestiona el tablero del juego.
Funciones: mostrar el tablero, verificar si una posición está libre, colocar una ficha, detectar si hay ganador o empate.

- **tateti.py**
 Reglas del juego y control de la partida.