from chessPictures import *
from interpreter import draw

# Fila superior: Caballo blanco y Caballo negro
fila_arriba = knight.join(knight.negative())

# Fila inferior: Caballo negro y Caballo blanco
fila_abajo = knight.negative().join(knight)

# Armamos el bloque poniendo la de arriba sobre la de abajo
resultado = fila_abajo.up(fila_arriba)

draw(resultado)