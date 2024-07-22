#este programa calcula y muestra el area de un circulo, utilizando 
#una función llamada calcular_area_circulo el cual recibe como 
#parámetro el radio y retorna el area calculada.

import math

def calcular_area_circulo(radio):
    area=math.pi*radio**2
    return area

#Llamada a la funcion
radio=(float(input('Escribe el radio del circulo y calcular su area: ')))
areaDelCirculo=calcular_area_circulo(radio)
print('El area del circulo es: ',round(areaDelCirculo,1))