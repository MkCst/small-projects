from random import choice

class Borracho:
    def __init__(self, nombre):
        self.nombre = nombre
    
class BorrachoTradicional(Borracho):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    # en realidad este metodo solo genera las nuevas coordenadas
    def camina(self):
        return choice([(0,1),(1,0),(-1,0),(0,-1)])
