import os
from random import uniform
from math import sqrt
from statics import Estadisticos
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
os.system("cls")


def estimar_pi(puntos):
    coor_points = [(uniform(-1,1), uniform(-1,1)) for _ in range(puntos)]
    in_circle = 0
    for i in coor_points:
        if sqrt(i[0]**2 + i[1]**2)<=1:
            in_circle+=1
    valor_pi = (4* in_circle) /puntos
    graficar(coor_points)
    #print(valor_pi)
    return valor_pi



def graficar(arreglo):
    in_circle = {"x_invalues": [i[0] for i in arreglo if sqrt(i[0]**2 +i[1]**2)<=1],
        "y_invalues": [i[1] for i in arreglo if sqrt(i[0]**2 +i[1]**2)<=1],
       }
    out_circle = { 
        "x_outvalues":[i[0] for i in arreglo if sqrt(i[0]**2 +i[1]**2)>1],
        "y_outvalues":[i[1] for i in arreglo if sqrt(i[0]**2 +i[1]**2)>1]
    }
    in_source = ColumnDataSource(data=in_circle)
    out_source = ColumnDataSource(data=out_circle)
    p = figure()
    p.circle(x='x_invalues', y='y_invalues', source=in_source, size=5, color="red")
    p.circle(x='x_outvalues', y='y_outvalues', source=out_source, size=5, color="navy")
    show(p)


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
        pi_array.append(estimar_pi(puntos))
    info_estd(pi_array)


crear_muestra(4)


