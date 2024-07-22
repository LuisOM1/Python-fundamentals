#crear una clase que manipule informacion de vehiculos y usando
#un método, imprima su ficha técnica.

class Vehiculo:
    def __init__(self,marca,tipo,modelo,color):
        self.marca=marca
        self.tipo=tipo
        self.modelo=modelo
        self.color=color
    
    def ficha_tecnica(self):
        print('---FICHA TÉCNICA DEL VEHICULO---')
        print('La marca del coche es: ',self.marca)
        print('El tipo del coche es: ',self.tipo)
        print('El modelo del coche es: ',self.modelo)
        print('El color del coche es: ',self.color)

#creamos el primer objeto
vehiculo=Vehiculo('Toyota','Tacoma','2023','Gris Mercurio')
print('\nImprimiremos los datos del Vehiculo: \n')
#Accedemos al método del primer objeto
vehiculo.ficha_tecnica()

#creamos el segundo objeto
vehiculo2=Vehiculo('Buick','Enclave','2023','Blanco')
print('\nImprimiremos los datos del Vehiculo 2\n')
#accederemos al método del segundo objeto
vehiculo2.ficha_tecnica()

#pedimos los datos para construir el tercer objeto
print('\n Ahora construye desde el teclado el tercer objeto:\n')
marca=input('Escribe la marca de tu vehiculo: ')
tipo=input('Escribe el tipo de tu vehiculo: ')
modelo=input('Escribe el modelo de tu vehiculo: ')
color=input('Escribe el color de tu vehiculo: ')

#construimos el tercer objeto
vehiculo3=Vehiculo(marca,tipo,modelo,color)
#accedemos al metodo del tercer objeto
print('\nLos datos del tercer vehiculo son:\n')
vehiculo3.ficha_tecnica()
