from coordenada import Coordenada


class Campo():
    def __init__(self):
        # Da la posicion del borracho
        self.coordenadas_borracho = {}
    
    def add_borracho(self, borracho, coordenada):
        self.coordenadas_borracho[borracho]=coordenada
    
    #Este metodo es el que mueve al borracho
    def mover_borracho(self, borracho):
        #Obtiene las coordenadas generadas
        delta_x, delta_y = borracho.camina()
        coordenada_actual = self.coordenadas_borracho[borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)
        self.coordenadas_borracho[borracho] = nueva_coordenada
        
    def obtener_coordenadas(self, borracho):
        return self.coordenadas_borracho[borracho]