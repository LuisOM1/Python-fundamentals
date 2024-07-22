class Circulo:
    def __init__(self,radio):
        self.radio=radio

    def area(self):
        return 3.14159 *self.radio *self.radio
    
#crearemos clases de objetos diferentes, con un método en común
#el método se llamará area()

class Circulo:
    def __init__(self, radio):
        self.radio=radio

    def area(self):
        return 3.14*(self.radio**2)
    
class Rectangulo:
    def __init__(self,alto,ancho):
        self.alto=alto
        self.ancho=ancho
    
    def area(self):
        return self.alto*self.ancho

class Triangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    
    def area(self):
        return (self.base*self.altura)/2

#crearemos una funcion que reciba un objeto, y verifique si tienen un
#metodo llamado calcular_area y lo ejecute, en caso contrario 
#avise que el método o función no están implementados

def calcular_area(objeto):
    if hasattr(objeto,'area'):
        return objeto.area()
    else:
        raise TypeError(
            'El objeto no tiene un método "area()" válido')

#creamos los objetos de su clase correspondiente
circulo=Circulo(5)
rectangulo=Rectangulo(4,3)
triangulo=Triangulo(5,9)

#invocamos el método calcular_area, para verificar si del objeto que
#le estamos pasando, existe un método llamado area, si es asi 
# que se ejecute
print('El area del circulo es: ',calcular_area(circulo))
print('El area del rectangulo es: ',calcular_area(rectangulo))
print('El area del triangulo es: ',calcular_area(triangulo)) 