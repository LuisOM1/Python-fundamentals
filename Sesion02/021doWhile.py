#El programa pedirá números para promediarlos
contador=0
suma=0
numero=0
while True:#do --- while  
    numero=float(input('Escribe un número para sumarlo (Ingresa 0 para salir) '))
    if(numero==0):
        break
    suma+=numero# suma=suma+numero
    contador+=1# contador=contador+1
#una vez que hayas salido del ciclo
if(contador>0):
    promedio=suma/contador
    print('La suma de los números es: ',suma)
    print('El total de números introducidos por el usuario son:',contador)
    print('El promedio de los números ingresados es: ',promedio)
else:
    print('No se ingresaron números válidos...')