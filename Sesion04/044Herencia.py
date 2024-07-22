#crearemos la super clase "figura" con un atributo (color)
#y un metodo llamado dibujar
class Figura:
    def __init__(self,color):
        self.color=color
    
    def dibujar(self):
        print(f'Estamos dibujando una figura de color:{self.color}.')

#crearemos la sub clase Rectangulo que hereda de la 
# superclase Figura
class Rectangulo(Figura):
    def __init__(self,color,ancho,alto):
        super().__init__(color)
        self.ancho=ancho
        self.alto=alto
    
    def calcular_area(self):
        return self.ancho*self.alto

#crearemos la sub clase Circulo que tambien hereda de la
#superclase figura
class Circulo(Figura):
    def __init__(self,color,radio):
        super().__init__(color)
        self.radio=radio

    def calcular_area(self):
        return 3.14*(self.radio**2)
    
print('Crearemos dos objetos que heredan de la super clase Figura\n'
      'uno de clase Rectangulo llamado mi_rectangulo\n y otro '
      'de clase Circulo llamado mi_circulo\n')

#creamos los objetos
mi_rectangulo=Rectangulo('Azul',5,3)
mi_circulo=Circulo('Amarillo',9)

#Usaremos los métodos de la clase mi_rectangulo
mi_rectangulo.dibujar()
print('La figura es de tipo rectangulo')
print('El color de la figura es',mi_rectangulo.color)
print('El area del rectangulo es: ',mi_rectangulo.calcular_area())

#usaremos los métodos del la clase mi_circulo
mi_circulo.dibujar()
print('La figura es de tipo circulo')
print('El color de la figura es: ',mi_circulo.color)
print('El area del circulo es: ',mi_circulo.calcular_area())