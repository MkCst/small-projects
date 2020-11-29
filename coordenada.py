class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def mover(self, delta_x, delta_y):
        return Coordenada(self.x + delta_x, self.y + delta_y)
    
    def distancia(self, coordenada):
        delta_x = self.x - coordenada.x
        delta_y = self.y - coordenada.y
        return (delta_x**2 + delta_y**2)**0.5
        
    