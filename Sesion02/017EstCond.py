#convertiremos de metros a kilómetros y a centímetros
#según lo solicite el usuario

distancia=float(input('Escribe la cantidad en metros: '))
opcion=input('\n A qué lo quieres convertir?'
             '\n a. Convertir a kilómetros'
             '\n b. Convertir a centímetros'
             '\n c. Convertir a pulgadas\n')
if opcion=='a':
    total=distancia/1000
    print('La cantidad convertida a kilómetros es: ',total)
elif opcion=='b':
    total=distancia*100
    print('LA cantidad convertida en centímetros es: ',total)
elif opcion=='c':
    total=(distancia*100)/2.54
    print('La cantidad convetida en pulgadas es: ', total)
else:
    print('Opción no válida...')