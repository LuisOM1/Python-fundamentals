#Crearemos un diccionario en el cual, cada clave tiene como su par (valor)
# otro diccionario dentro

print('Este es un diccionario de tipo [clave: valor], pero dentro del valor guarda otro \n'
      'diccionario, es algo asi: [clave:[clave:valor]]')
empleados={
    "001":{'nombre':'Juan','edad':30,'puesto':'Administrador'},
    "002":{'nombre':'Maria','edad':25,'puesto':'Analista'},
    "003":{'nombre':'Pedro','edad':35,'puesto':'Desarrollador'},
}

print('Información del empleado con código 002:')
print('Nombre: ',empleados['002']['nombre'])
print('Edad: ',empleados['002']['edad'])
print('Puesto: ',empleados['002']['puesto'])

empleados['004']={'nombre':'Laura','edad':28,'puesto':'diseñadora'}

print('\nInformación de todos los empleados: \n')
for codigo, info in empleados.items():
    print('codigo:',codigo)
    print('nombre:',info['nombre'])
    print('edad:',info['edad'])
    print('puesto:',info['puesto'])
    print("-" * 20)
    print('\n')