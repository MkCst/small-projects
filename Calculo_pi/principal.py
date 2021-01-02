import os
from random import uniform
from math import sqrt
from statics import Estadisticos
from bokeh.plotting import figure, output_file, show
os.system("cls")

tries = 10

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
    valor_pi = (4 * (len(in_circle_x)+ len(in_circle_y)))/puntos
    return (valor_pi, in_circle_x, in_circle_y, out_circle_x, out_circle_y)
    
def crear_muestra(tries):
    pi_array = []
    for i in range(tries):
        pi_valor, in_x, in_y, out_x, out_y = estimar_pi(puntos)
        pi_array.append(pi_valor)
    return (pi_array, in_x, in_y, out_x, out_y)
tries = 10
puntos = 100
deviation = 1
presicion = 0.1
iteracion = 1
stds = Estadisticos()

while deviation >=(presicion/1.96):
    pi_array, in_x, in_y, out_x, out_y = crear_muestra(tries)
    desviacion = stds.std_desv(pi_array)
    varianza = stds.variance(pi_array)
    media = stds.mean(pi_array)
    print(f"iteraccion: {iteracion}")
    print(f"Desviacion estandar: {desviacion}")
    print(f"Varianza: {varianza}")
    print(f"Media: {media}")
    print(f"intentos: {tries}\t Puntos: {puntos}")
    puntos *= 10
    tries *= 10
    iteracion +=1