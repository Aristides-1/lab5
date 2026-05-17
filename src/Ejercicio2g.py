from chessPictures import *
from interpreter import draw

square_black = square.negative()
fila_A = square.join(square_black).horizontalRepeat(4)
fila_B = square_black.join(square).horizontalRepeat(4)

#Definimos las piezas en hileras de texto puras
piezas_blancas_base = rock.join(knight).join(bishop).join(queen).join(king).join(bishop).join(knight).join(rock)
peones_blancos_base = pawn.horizontalRepeat(8)

piezas_negras_base = piezas_blancas_base.negative()
peones_negros_base = peones_blancos_base.negative()

# Las montamos transparentemente SOBRE sus casilleros de fondo correspondientes
fila_1 = fila_A.under(piezas_negras_base) # Fila 8 real (Negras)
fila_2 = fila_B.under(peones_negros_base) # Fila 7 real (Peones Negros)
fila_7 = fila_A.under(peones_blancos_base) # Fila 2 real (Peones Blancos)
fila_8 = fila_B.under(piezas_blancas_base) # Fila 1 real (Blancas)

#El centro vacío del tablero (4 filas sin piezas)
centro_vacio = fila_A.up(fila_B).verticalRepeat(2)

#Construimos el tablero completo apilando todo de abajo hacia arriba
resultado = fila_8.up(fila_7).up(centro_vacio).up(fila_2).up(fila_1)

draw(resultado)