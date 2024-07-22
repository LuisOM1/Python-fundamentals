#Este programa ejemplifica el uso de la instruccion break, de la sig.
#Forma: debería ejecutarse un ciclo del 1 al 10 e imprimir cada numero
#pero usando la instrucción break, haremos que cuando el contador llegue
#al numero 6, se salga del ciclo

for i in range(1,11):
    if(i==6):
        print('adios...')#
        break
    print('i vale: ',i)