#crearemos un arreglo bidimensional de 3 x 3, lo llenaremos con datos
#introducidos desde el teclado  y mostraremos su contenido.

filas=3
columnas=3

matriz=[[5]*columnas for _ in range(filas)]

for i in range (filas):
    for j in range (columnas):
        dato=input("Ingrese el dato para la posicion ({},{}): "
                   .format(i,j))
        matriz[i][j]=dato

print('Los datos del arreglo bidimensional son: ')
for fila in matriz:
    print(fila)

#imprimir la diagonal principal
for i in range(3):
    for j in range(3):
        if i==j:
            print(matriz[i][j])

for i in range(2,-1,-1):
    for j in range(2,-1,-1):
        if i==j:
            print(matriz[i][j])
