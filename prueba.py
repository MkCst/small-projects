from bokeh.plotting import figure, show, output_file
from random import  randint

if __name__ == "__main__":
    output_file("Grafica simple.html")
    figu= figure()
    ejex = [randint(1,10) for _ in range(10)]
    ejey = [randint(1,20) for _ in range(10)]
    
    figu.line(ejex,ejey, line_width =2)
    show(figu)
