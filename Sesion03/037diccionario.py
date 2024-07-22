#el presente programa manipula una estructura de datos llamada diccionario, 
# que maneja pares de tipo clave, valor

diccionario={}

diccionario['nombre']='Antonio'
diccionario['edad']=31
diccionario['ciudad']='Veracruz'

print(diccionario)

print('El nombre del usuario es: ',diccionario['nombre'])
print('La edad del usuario es: ',diccionario['edad'])
print('La ciudad del usuario es: ',diccionario['ciudad'])

print('se actualizarán algunos datos:\n')

diccionario['edad']=35

print(diccionario)

print('Eliminaremos el elemento ciudad del diccionario: ')
del diccionario['ciudad']

print(diccionario)

if 'nombre' in diccionario:
    print('la clave "nombre" existe en el diccionario')

if 'ciudad' in diccionario:
    print('la clave "ciudad" existe en el diccionario')
else:
    print('la clave "ciudad" NO existe en el diccionario')

cantidadElementos=len(diccionario)
print('El diccionario tiene: ', cantidadElementos," Elementos")

for clave, valor in diccionario.items():
    print(clave+ " : ",valor)