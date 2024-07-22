#crearemos un programa que nos muestre como se programa
#la herencia en python

#crearemos la super clase, o clase padre o clase base
class Animal:
    def __init__(self,nombre):
        self.nombre=nombre

    def comer(self):
        print(f'{self.nombre} está comiendo.')

#crearemos la sub clase o clase hija o clase derivada
class Perro(Animal):
    def __init__(self,nombre,raza):
        super().__init__(nombre)
        self.raza=raza

    def ladrar(self):
        print(f'{self.nombre} es de la raza {self.raza}'
              ' y esta ladrando.')

#crearemos un objeto de la clase Perro
print('Crearemos el objeto mi_perro de clase Perro,\n'
      'que hereda atributos de la super clase Animal,\n'
      'su nombre es: Simba, su raza es: Labrador')
mi_perro=Perro('Simba','Labrador')
mi_perro.comer()#este método se hereda de la super clase
mi_perro.ladrar()#este metodo es propio de la sub clase