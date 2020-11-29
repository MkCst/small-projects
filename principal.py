
from random import randint
from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada
from bokeh.plotting import figure, show, output_file
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
    output_file("Camino_aleatorio.html")
    grafica = figure(
        title = "Camino aleatorio",
        x_axis_label= "pasos",
        y_axis_label= "distancia recorrida"
    )
    grafica.line(x, y, legend_label="distancia media")
    show(grafica)

if __name__ == "__main__":
    print("hola bienvenido!")
    distancia_por_caminata = []
    distancias_caminata = [10,100,1000]
    intentos = 10
    
    for pasos in distancia_por_caminata:
        distancias  = simular_caminata(pasos, intentos,BorrachoTradicional ) 
        distancia_media = round(sum(distancias)/len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        
        distancia_por_caminata.append(distancia_media)
        
        print(f"{BorrachoTradicional.__name__} caminata aleatoria de {pasos} pasos")
        print(f"Media: {distancia_media}")
        print(f"Minima: {distancia_minima}")
        print(f"Maxima: {distancia_maxima}")
        print()
        graficar(distancias_caminata, distancia_por_caminata)
    print("adios")
    