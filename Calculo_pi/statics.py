from math import sqrt, exp, pi

class Estadisticos:

    def __init__(self, elements):
        self.v_media = self.mean(elements)
        self.v_varianza = self.variance(elements)
        self.v_stdvcion = self.std_desv(elements) #Desviacion estandar
        self.distribucion_normal = self.normal_distr(elements)

    def mean(self, elements):
        return sum(elements)/len(elements)

    def variance(self, elements):
        var_med = self.mean(elements)
        sum_items = 0
        for i in elements:
            sum_items+=(i - var_med)**2
        return sum_items/ len(elements)

    def std_desv(self, elements):
        return sqrt(self.variance(elements)) 

    def normal_distr(self, elemets):
        distrib = []
        for i in elemets:
            op1 = 1 / (self.v_stdvcion * sqrt(2*pi))
            op2 = exp(-1/2*((i - self.v_media)/ self.v_stdvcion)**2)
            distrib.append(op1*op2)
        return distrib