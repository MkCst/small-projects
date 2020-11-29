from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada
from bokeh.plotting import figure, show
# Metodos que serviran para modelar en la clase principal

def caminata(campo, borracho, pasos):
    """obtiene toda la caminata y la distancia total """
    inicio = campo.obtener_coordenadas(borracho)
    for _ in range(pasos):
        campo.mover_borracho(borracho)
    #Devulve la distancia entre la primera hasta la ultima posicion
    return inicio.distancia(campo.obtener_coordenadas(borracho))

def simular_caminata(pasos, intentos, BorrachoTradicional):
    borracho = BorrachoTradicional(nombre="mike")
    origen = Coordenada(0,0)
    distancias = []
    
    for _ in range(intentos):
        campo = Campo()
        campo.add_borrachos(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata,1))
    return distancias

def graficar(x, y):
    grafica = figure(
        title = "Camino aleatorio",
        x_axis_label= "pasos",
        y_axis_label= "distancia recorrida"
    )
    grafica.line(x,y, legend="distancia media")
    show(grafica)