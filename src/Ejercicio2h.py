from chessPictures import *
from interpreter import draw

#Definimos los casilleros base intercalados
square_black = square.negative()
fila_par = square.join(square_black).horizontalRepeat(4)
fila_impar = square_black.join(square).horizontalRepeat(4)

#Creamos hileras de piezas puras (blancas y negras)
piezas_blancas = rock.join(knight).join(bishop).join(queen).join(king).join(bishop).join(knight).join(rock)
piezas_negras = piezas_blancas.negative()
peones_blancos = pawn.horizontalRepeat(8)
peones_negros = peones_blancos.negative()

#Construimos cada una de las 8 filas del tablero según la apertura Italiana
f8 = fila_par.under(piezas_negras)
f7 = fila_impar.under(peones_negros)

#Contiene al Caballo Negro en c6 (posición 3)
p_f6 = square.join(square_black).join(knight.negative()).join(square_black).join(square).join(square_black).join(square).join(square_black)
f6 = fila_par.under(p_f6)

#Contiene al Peón Negro en e5 (posición 5)
p_f5 = square_black.join(square).join(square_black).join(square).join(pawn.negative()).join(square).join(square_black).join(square)
f5 = fila_impar.under(p_f5)

#Contiene al Alfil Blanco en c4 (posición 3) y Peón Blanco en e4 (posición 5)
p_f4 = square.join(square_black).join(bishop).join(square_black).join(pawn).join(square_black).join(square).join(square_black)
f4 = fila_par.under(p_f4)

#Contiene al Caballo Blanco en f3 (posición 6)
p_f3 = square_black.join(square).join(square_black).join(square).join(square_black).join(knight).join(square_black).join(square)
f3 = fila_impar.under(p_f3)

#Peones blancos restantes (faltan c y e)
p_f2 = pawn.join(pawn).join(square).join(pawn).join(square).join(pawn).join(pawn).join(pawn)
f2 = fila_par.under(p_f2)

#Piezas blancas restantes (falta b, c y f)
p_f1 = rock.join(square).join(square).join(queen).join(king).join(square).join(square).join(rock)
f1 = fila_impar.under(p_f1)

#Apilamos todo verticalmente de abajo hacia arriba
tablero_italiano = f1.up(f2).up(f3).up(f4).up(f5).up(f6).up(f7).up(f8)
draw(tablero_italiano)