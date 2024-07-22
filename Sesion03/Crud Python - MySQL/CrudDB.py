# pip install mysql-connector-python

#recuerda que debes crear una base de datos en mysql llamada pruebaperu
#create database pruebaperu;
#entrar a esa base de datos
#use pruebaperu;
#y dentro una tabla llamada datos
#create table datos(dato varchar(70));
#despues de esto, el programa debe funcionar

import os
import time
import mysql.connector
#debes descargar el conector con esta instrucción: pip install mysql.connector desde el cmd
#de windows o la terminal de tu sistema operativo

# Conexión a la base de datos
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123',
    database='pruebaperu',
    port= '3307'
)
#Un cursor se utiliza para ejecutar comandos SQL en la base de datos
mycursor = mydb.cursor()
#creamos el menu
while True:
    print('--MENU DEL SISTEMA--'
          '\n1. Insertar un registro'
          '\n2. Eliminar un registro'
          '\n3. Buscar un registro'
          '\n4. Sobreescribir un registro'
          '\n5. Mostrar el contenido de la Base de Datos'
          '\n6. Salir del sistema')
    opcion=int(input('Elige una opción: '))
    if opcion==1:#create (insertar)
        dato=input('Ingresa el dato a insertar: ')
        #creamos la instruccion sql que permitirá insertar en la bd 
        #%s porque es solo un valor 
        sql='INSERT INTO datos (dato) VALUES (%s)'
        #se crea la tupla con el único valor que se insertará
        val=(dato,)
        mycursor.execute(sql,val)#ejecuta la consulta sql
        mydb.commit()#confirma los cambios en la base de datos
        #imprime el número de registros que se han insertado
        print(mycursor.rowcount,'Registro insertado')
        time.sleep(2)
        os.system('cls')
    elif opcion==2:#Delete (eliminar)
        dato=input('Ingresa el dato a eliminar')
        #se crea la instruccion sql a ejecutar
        sql='DELETE FROM datos WHERE dato=%s'
        #se crea la tupla llamada val que contiene el dato que el usuario ingresó
        #para eliminarlo
        val=(dato,)
        #se ejecuta la consulta de eliminación
        mycursor.execute(sql,val)
        #se confirman los cambios en la bd
        mydb.commit()
        #se imprime el numero de registros que se eliminaron
        print(mycursor.rowcount,'registro(s) eliminado(s)')
        time.sleep(2)
        os.system('cls')
    elif opcion==3:#Read (leer)
        dato=input('Ingresa el dato a buscar: ')
        #crea una consulta de seleccion
        sql='SELECT * FROM datos WHERE dato=%s'
        #crea la tupla
        val=(dato,)
        #ejecuta la instrucción con la tupla
        mycursor.execute(sql,val)
        #verifica si existe algún resultado
        myresult=mycursor.fetchall()
        if myresult:
            print('El dato está en la tabla.')
        else:
            print('El dato no existe en la tabla.')
        time.sleep(2)
        os.system('cls')
    elif opcion==4:#update (actualizar)
        #pedimos el dato existente para actualizar
        datoAnterior=input('Ingresa el dato a sobreescribir: ')
        #pedimos el nuevo dato que irá en su lugar
        datoNuevo=input('Ingresa el dato nuevo: ')
        #creamos una consulta de actualización
        sql='UPDATE datos SET dato=%s WHERE dato=%s'
        #se crea la tupla con los datos el nuevo y el que se eliminará
        val=(datoNuevo,datoAnterior)
        #se ejecuta la consulta
        mycursor.execute(sql,val)
        #se confirman los cambios en la bd
        mydb.commit()
        #imprime el número de registros actualizados en la bd
        print(mycursor.rowcount,'registro(s) actualizado(s)')
        time.sleep(2)
        os.system('cls')
    elif opcion==5:#Read (leer)
        #crea una consulta de seleccion en la tabla datos
        mycursor.execute('SELECT * FROM datos')
        #se utiliza el método fetchall para obtener todos los resultados de la consulta
        myresult=mycursor.fetchall()
        #mostraremos el contenido de la tabla
        print('Contenido de la tabla:')
        #inicia el ciclo que recorre los resultados guardados en myresult
        for x in myresult:
            #imprime cada fila o registro
            print(x)
        time.sleep(2)
        os.system('cls')
    elif opcion == 6:  # salir del sistema
        respuesta = input('Estás seguro? (s/n)')
        if respuesta.upper() == 'S':
            print('Saliendo del sistema...')
            time.sleep(2)
            os.system('cls')
            break
        time.sleep(2)
        os.system('cls')
    else:
        print('Opción no válida, intenta de nuevo...')
        time.sleep(2)
        os.system('cls')

# Cerrar la conexión
mydb.close()

