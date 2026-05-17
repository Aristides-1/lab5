from chessPictures import *
from interpreter import draw

#Empieza por casillero negro para que el patrón quede correcto
square_black = square.negative()
par_casilleros = square.join(square_black)
#Repetimos el patrón de dos casilleros 4 veces para llegar a 8
resultado = par_casilleros.horizontalRepeat(4)

draw(resultado)