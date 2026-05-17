from chessPictures import *
from interpreter import draw

#la torre es blanca, con negative se vuelve negra
torre_negra = rock.negative()
draw(torre_negra)