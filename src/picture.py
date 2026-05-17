from colors import *

class Picture:
  def __init__(self, img):
    self.img = img

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for fila in self.img:
        vertical.append(fila[::-1])
    return Picture(vertical)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    return Picture(self.img[::-1])

  def negative(self):
    """ Devuelve un negativo de la imagen """
    #Creamos una lista vacía para almacenar las nuevas filas con colores invertidos
    negativo = []
    
    #Recorremos fila por fila el atributo interno self.img
    for fila in self.img:
        #Para cada carácter en la fila, llamamos a _invColor y los unimos de nuevo en un string
        nueva_fila = "".join([self._invColor(caracter) for caracter in fila])
        negativo.append(nueva_fila)
        
    #Retornamos un nuevo objeto Picture con la representación modificada
    return Picture(negativo)

  def join(self, p):
    return Picture(None)

  def up(self, p):
    return Picture(None)

  def under(self, p):
    return Picture(None)
  
  def horizontalRepeat(self, n):
    return Picture(None)

  def verticalRepeat(self, n):
    return Picture(None)