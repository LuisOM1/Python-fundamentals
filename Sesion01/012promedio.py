#el programa muestra y calcula el promedio de las calificaciones
#de un alumno
print('El programa calculará el promedio de tus 3 calificaciones\n')
nombre=input('Escribe tu nombre alumno: ')
mat=float(input('Escribe tu calificación de matemáticas: '))
fis=float(input('Escribe tu calificación de física: '))
quim=float(input('Escribe tu calificación de química: '))
'''
prioridad de  operadores aritméticos
() y ** primer lugar
* y /   segundo lugar
+ -     tercer lugar
'''

prom=(mat+fis+quim)/3

print(f'{nombre} tu promedio es: {round(prom,2)}')