from chessPictures import *
from interpreter import draw

square_black = square.negative()

#Creamos las dos hileras tipo de 8 casilleros
fila_par = square.join(square_black).horizontalRepeat(4)
fila_impar = square_black.join(square).horizontalRepeat(4)

#Juntamos ambas filas en un bloque de 2 de alto
bloque_base = fila_impar.up(fila_par)

#Repetimos ese bloque 4 veces verticalmente para obtener las 8 filas del tablero
tablero_vacio = bloque_base.verticalRepeat(4)

draw(tablero_vacio)