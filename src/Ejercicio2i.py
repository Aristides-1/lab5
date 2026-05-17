from chessPictures import *
from interpreter import draw

square_black = square.negative()
fila_par = square.join(square_black).horizontalRepeat(4)
fila_impar = square_black.join(square).horizontalRepeat(4)

piezas_blancas = rock.join(knight).join(bishop).join(queen).join(king).join(bishop).join(knight).join(rock)
piezas_negras = piezas_blancas.negative()
peones_blancos = pawn.horizontalRepeat(8)
peones_negros = peones_blancos.negative()

#Construimos las 8 filas adaptadas a la Apertura Escocesa
f8 = fila_par.under(piezas_negras)
f7 = fila_impar.under(peones_negros)

#Caballo Negro en c6
p_f6 = square.join(square_black).join(knight.negative()).join(square_black).join(square).join(square_black).join(square).join(square_black)
f6 = fila_par.under(p_f6)

#Peón Negro en e5
p_f5 = square_black.join(square).join(square_black).join(square).join(pawn.negative()).join(square).join(square_black).join(square)
f5 = fila_impar.under(p_f5)

#Peón Blanco en d4 (posición 4) y Peón Blanco en e4 (posición 5)
p_f4 = square.join(square_black).join(square).join(pawn).join(pawn).join(square).join(square_black).join(square)
f4 = fila_par.under(p_f4)

#Caballo Blanco en f3
p_f3 = square_black.join(square).join(square_black).join(square).join(square_black).join(knight).join(square_black).join(square)
f3 = fila_impar.under(p_f3)

#Peones blancos restantes (faltan d y e)
p_f2 = pawn.join(pawn).join(pawn).join(square).join(square).join(pawn).join(pawn).join(pawn)
f2 = fila_par.under(p_f2)

#Piezas blancas restantes (falta f)
p_f1 = rock.join(knight).join(bishop).join(queen).join(king).join(square).join(knight).join(rock)
f1 = fila_impar.under(p_f1)

tablero_escoces = f1.up(f2).up(f3).up(f4).up(f5).up(f6).up(f7).up(f8)
draw(tablero_escoces)