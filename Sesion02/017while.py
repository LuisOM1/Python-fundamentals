# simularemos el conteo regresivo del despegue de un cohete

import time

contador=10

while contador>0:
    print(contador)   
    time.sleep(1)
    contador-=1       

print('El cohete ha despegado...')
print('Exito en su misión...')
