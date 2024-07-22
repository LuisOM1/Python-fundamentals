numeros=[] #lista vacia
contador=0
#el usuario ingresará los datos

for i in range(10):
    numero=float(input('Ingresa un número: '))
    numeros.append(numero)
    contador+=1

#calcularemos la suma
suma=sum(numeros)

#mostrar la suma de los numeros al usuario
print('La suma de los números introducidos es: ',suma)
print('Los números introducidos fueron: ',contador)