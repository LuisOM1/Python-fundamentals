'''
estructuras selectivas
if          if -- else          if--- elif ---elif ---elif --- else

estructuras repetitivas
while 
do -- while (en python no existe de forma nativa pero se puede implementar)
for 
caracteristicas:
while -- puede que nunca se ejecute
do -- while --- al menos una vez se va a entrar a este ciclo
for -- casi siempre que se entra al ciclo, se sabe cuantas veces se va
        a repetir, es muy utilizado para manipular estructuras de datos 
'''
#Simularemos el conteo regresivo del despegue de un cohete
import time

contador=10

print('Inicia el conteo regresivo...')
while contador>0:
    print(contador)
    time.sleep(1)
    contador-=1#    contador=contador-1
print('El cohete ha despegado con exito...')
