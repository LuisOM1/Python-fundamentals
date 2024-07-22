#Este programa crea la clase triangulo con metodo para
#calcular su area

class Triangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    
    def area(self):
        return (self.base*self.altura)/2

#pediremos los datos necesarios para crear un objeto de clase triangulo
base=int(input('Escribe la base del triangulo: '))
altura=int(input('Escribe la altura del triangulo: '))

#construimos el objeto
triangulo=Triangulo(base,altura)
#invocamos el método area del objeto triangulo
print(triangulo.area())