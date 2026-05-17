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
    # Invierte el orden de las filas (de arriba a abajo)
    return Picture(self.img[::-1])

  def negative(self):
    return Picture(None)

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