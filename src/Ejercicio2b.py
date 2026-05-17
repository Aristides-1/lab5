from chessPictures import *
from interpreter import draw

fila_arriba = knight.join(knight.negative())

#Los caballos de abajo usan el negativo y además se voltean horizontalmente
caballo_inf_izq = knight.negative().verticalMirror()
caballo_inf_der = knight.verticalMirror()
fila_abajo = caballo_inf_izq.join(caballo_inf_der)

resultado = fila_abajo.up(fila_arriba)

draw(resultado)