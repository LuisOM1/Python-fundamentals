#El programa evaluará la estatura del usuario y 
#si la estatura es menor que 160 cms imprimirá: Eres chaparrito
#si la estatura es entre 160 y entre 175 cms imprimirá: Eres de estatura
#mediana
# si la estatura es mayor a 175 cms imprimirá: Eres alto

nombre=input('Escribe tu nombre: ')
estatura=int(input('Escribe tu estatura en centimetros: '))

if (estatura<160):
    print(f'{nombre} Eres chaparrito...')
    print(nombre,'Eres chaparrito',nombre,'otro')
    print(f'{nombre} texto {nombre} texto2 {nombre}')

if (estatura>=160) and (estatura<=175):
    print(f'{nombre} Eres de estatura mediana...')

if(estatura>175):
    print(f'{nombre} Eres de estatura alta...')


'''
if(condicion):
    acciones

if(condicion):
    acciones1
else
    acciones2

if (condicion1):
    acciones A
elif(condicion2):
    acciones B
elif(condicion3):
    acciones C
else:
    acciones X
'''