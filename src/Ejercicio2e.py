from chessPictures import *
from interpreter import draw

square_black = square.negative()
par_invertido = square_black.join(square)

#Repetimos el patrón de dos casilleros 4 veces para llegar a 8
resultado = par_invertido.horizontalRepeat(4)
draw(resultado)