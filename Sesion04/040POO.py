#Crearemos la clase persona, esto es un "molde" para crear objetos
#de este tipo
class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad

    def saludar(self):
        print(f'Hola, mi nombre es {self.nombre} '
              f'y tengo {self.edad} años.')

# Crearemos los objetos de la clase Persona
persona1=Persona('Juan',25)
persona2=Persona('Maria',31)
print()

#Accederemos a los atributos de estos objetos
print('El nombre de la persona 1 es: ',persona1.nombre)
print('La edad de la persona 1 es: ',persona1.edad)
print(f'El nombre y edad de la persona2 son: {persona2.nombre} y '
      f'{persona2.edad}')

#accederemos a los métodos de estos objetos
persona1.saludar()
persona2.saludar()