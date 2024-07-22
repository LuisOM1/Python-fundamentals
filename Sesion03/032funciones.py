def es_par(numero):
    if numero%2 ==0:
        return True
    else:
        return False
    
numero=int(input('Escribe un número y determinaré si es par o impar: '))
if es_par(numero):
    print(f'El numero {numero} es par')
else:
    print(f'El numero {numero} es impar')