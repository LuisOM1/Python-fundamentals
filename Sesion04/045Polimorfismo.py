#crearemos un ejemplo de polimorfismo
#creamos la super clase Animal con el encabezado de una función 
#pero sin el cuerpo de la función, como las interfaces de java
class Animal:
    def comunicarse(self):
        raise NotImplementedError(
            'La subclase debe implementar el método comunicarse()')

#creamos las subclases que heredan el método comunicarse
#pero lo implementan de diferente forma, decir, el cambian
#la forma, es decir hacen polimorfismo
class Perro(Animal):
    def comunicarse(self):
        return 'Soy un Perro y ladro, Guauu!'
    
class Gato(Animal):
    def comunicarse(self):
        return 'Soy un gato y maullo, Miauu!'
    
class Oso(Animal):
    def comunicarse(self):
        return 'Soy un oso y grullo, Ggrrr!'

#como tenemos varios objetos con métodos comunes, podemos meterlos
#a una lista
animales=[Perro(),Gato(),Oso()]
#y recorrerlos
for animal in animales:
    print(animal.comunicarse())