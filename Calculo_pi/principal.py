import os
from random import uniform
from math import sqrt
from statics import Estadisticos
from bokeh.plotting import figure, output_file, show
os.system("cls")


def estimar_pi(puntos):
    in_circle_x = []
    in_circle_y = []
    out_circle_x = []
    out_circle_y = []
    pi_array = [] 
    # Se encuentra dentro del circulo 
    for i in range(puntos):
        pos_x = uniform(-1,1)
        pos_y = uniform(-1,1)
        
        if sqrt(pos_x**2 +pos_y**2)<=1:
            in_circle_x.append(pos_x)
            in_circle_y.append(pos_y)
        else:
            out_circle_x.append(pos_x)
            out_circle_y.append(pos_y)
    # Pi estimado
    valor_pi = (4 * len(in_circle_x))/puntos
    graficar(in_circle_x, in_circle_y, out_circle_x, out_circle_y)
    return valor_pi

def graficar(in_x, in_y, out_x, out_y):
    output_file("pipi.html")
    plot = figure(plot_width=600, plot_height=600)
    plot.circle(in_x, in_y, size=5, color="red", alpha = 0.5)
    plot.circle(out_x, out_y, size=5, color="navy", alpha = 0.5)
    show(plot)


def info_estd(arreglo):
    #Creacion del objeto para obtener los estadisticos del arreglo
    stds = Estadisticos()
    print("Los valores de pi resultantes son: ")
    for i in arreglo:
        print(i,end="| ")
    print()
    desviacion = stds.std_desv(arreglo)
    varianza = stds.variance(arreglo)
    media = stds.mean(arreglo)
    print(f"Desviacion estandar: {desviacion}")
    print(f"Varianza: {varianza}")
    print(f"Media: {media}")


def crear_muestra(tries):
    #Valores de pi
    pi_array = []
    for i in range(tries):
        puntos = int(input("Cuantos puntos tendra su muestra: "))
        pi_valor = estimar_pi(puntos)
        pi_array.append(pi_valor)
    info_estd(pi_array)


crear_muestra(4)


