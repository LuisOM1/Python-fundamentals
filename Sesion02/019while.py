#El programa pedirá números y los irá sumando en una variable que 
#tecnicamente se conoce como acumulador
suma=0
numero=1

while numero !=0:
    numero=int(input('Ingresa un numero para sumarlo, (ingresa 0 para salir): '))
    suma+=numero# suma=suma+numero

print('La suma de los números introducidos es: ',suma)