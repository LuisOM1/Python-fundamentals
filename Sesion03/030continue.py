#ejemplificaremos el uso de la instruccion continue, el programa
#imprimirá numeros del 1 al 10, pero omitirá la impresión cuando
#el modulo de la división sea igual a cero, es decir cuando el 
#numero sea par.

for i in range(1,11):
    if i%2==0:
        print('impresión omitida por ser numero par...')#
        continue
    print('i vale: ',i)