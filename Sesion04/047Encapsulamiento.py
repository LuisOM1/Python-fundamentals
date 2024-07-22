class Persona:
    def __init__(self, nombre, edad):
        self._nombre=nombre
        self._edad=edad

    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self,nombre):
        self._nombre=nombre
    
#este es un ejemplo de polimorfismo, crearemos la clase Persona
#con métodos get y set para leer y escribir en sus atributos

class Persona:
    def __init__(self,nombre,edad):
        self._nombre=nombre
        self._edad=edad

#leemos el atributo nombre    
    def get_nombre(self):
        return self._nombre

#escribimos en el atributo nombre
    def set_nombre(self,nombre):
        self._nombre=nombre

#leemos el atributo edad
    def get_edad(self):
        return self._edad
    
#escribimos el atributo edad, con una pequeña validacion
    def set_edad(self,edad):
        if (edad>0 and edad<100):
            self._edad=edad

#creamos la instancia (objeto) de la clase Persona, llamada persona
persona=Persona('Carlos',25)
print('\nLa persona registrada en esta instancia es:'
      f' {persona.get_nombre()} y tiene {persona.get_edad()} años')

print('\n sobreescribiremos los datos anteriores' 
      'de la misma instancia\n')

persona.set_nombre('Mario')
persona.set_edad(31)

print('Los datos actualizados de la misma instancia son: '
      f'{persona.get_nombre()} y tiene {persona.get_edad()}\n')
