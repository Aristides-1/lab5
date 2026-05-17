from colors import *

class Picture:
    def __init__(self, img):
        self.img = img

    def __eq__(self, other):
        return self.img == other.img

    def _invColor(self, color):
        if color not in INVERTED:
            return color
        return INVERTED[color]

    def verticalMirror(self):
        """ Devuelve el espejo vertical de la imagen """
        vertical = []
        for value in self.img:
            vertical.append(value[::-1])
        return Picture(vertical)

    def horizontalMirror(self):
        """ Devuelve el espejo horizontal de la imagen """
        return Picture(self.img[::-1])

    def negative(self):
        """ Devuelve un negativo de la imagen """
        nuevo_img = []
        for fila in self.img:
            nueva_fila = "".join([self._invColor(char) for char in fila])
            nuevo_img.append(nueva_fila)
        return Picture(nuevo_img)

    def join(self, p):
        """ Devuelve una nueva figura poniendo la figura del argumento 
            al lado derecho de la figura actual """
        return Picture([f1 + f2 for f1, f2 in zip(self.img, p.img)])

    def up(self, p):
        """ Devuelve una nueva figura poniendo la figura p encima de la actual """
        return Picture(p.img + self.img)

    def under(self, p):
        """ Devuelve una nueva figura poniendo la figura p sobre la
            figura actual """
        nueva_img = []
        for f_fondo, f_frente in zip(self.img, p.img):
            linea = "".join([c_frente if c_frente != ' ' else c_fondo for c_fondo, c_frente in zip(f_fondo, f_frente)])
            nueva_img.append(linea)
        return Picture(nueva_img)
  
    def horizontalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual al costado """
        return Picture([fila * n for fila in self.img])

    def verticalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual abajo """
        return Picture(self.img * n)