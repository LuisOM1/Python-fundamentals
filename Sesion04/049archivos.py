import os
def crear_archivo(nombreArchivo):
    try:
        archivo=open(nombreArchivo,'w')
        archivo.close()
        print('Se ha creado el archivo: ',nombreArchivo,'\n')
    except IOError:
        print('Ocurrió un error al crear el archivo: ',nombreArchivo)

def agregar_texto(nombreArchivo,texto):
    try:
        archivo=open(nombreArchivo,'a')
        archivo.write(texto+'\n')
        archivo.close()
        print(f'Se ha agregado el texto \n{texto}\n al archivo: '
              ,nombreArchivo,'\n')
    except IOError:
        print('Error al agregar texto al archivo: ',nombreArchivo)

def eliminar_texto(nombreArchivo,texto):
    try:
        archivo=open(nombreArchivo,'r')
        lineas=archivo.readlines()
        archivo.close()

        archivo=open(nombreArchivo,'w')
        for linea in lineas:
            if linea.strip() !=texto:
                archivo.write(linea)
        archivo.close()
        print(f'Se ha eliminado el texto \n{texto}\n del archivo: '
              ,nombreArchivo,'\n')
    except IOError:
        print('Error al eliminar texto del archivo: ',nombreArchivo)

def buscar_texto(nombreArchivo,texto):
    try:
        archivo=open(nombreArchivo,'r')
        lineas=archivo.readlines()
        archivo.close()

        encontrado=False
        for linea in lineas:
            if texto in linea:
                encontrado=True
                print(f'El texto: \n{texto}\n encontrado: ',linea.strip(),'\n')
        if not encontrado:
            print('No se encontró el texto en el archivo: ',nombreArchivo)
    except IOError:
        print('Error al buscar texto en el archivo: ',nombreArchivo)

#inicia el programa
nombreArchivo='miArchivo.txt'
#creamos el archivo
os.system('cls')
crear_archivo(nombreArchivo)
#agregamos texto al archivo
agregar_texto(nombreArchivo,'Erase una vez en un pais lejano')
agregar_texto(nombreArchivo,'un rey que vivia muy feliz')
agregar_texto(nombreArchivo,'dentro de un enorme castillo')
#buscamos texto
buscar_texto(nombreArchivo,"castillo")
#eliminamos texto
eliminar_texto(nombreArchivo,'dentro de un enorme castillo')
#buscamos el texto nuevamente
buscar_texto(nombreArchivo,"castillo")
