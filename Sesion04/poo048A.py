#crearemos una clase normal, para despues accederla desde otro 
#archivo de programa.
class Usuarios:
    tipoUsuario='Free'
    publicidad=True

    def __init__(self,id,alias,nombre,apellidos):
        self.id=id
        self.alias=alias
        self.nombre=nombre
        self.apellidos=apellidos

    def muestra_datos(self):
        print('El id del usuario es: ',self.id)
        print('El alias del usuarios es: ',self.alias)
        print('El nombre y apellidos del usuario son: '
              f'{self.nombre} {self.apellidos}')
        
#crearemos un objeto de clase Usuarios
# ocultaremos estas lineas al crear los otros archivos
usuario=Usuarios(13,'Fer','Fernando','Cruz')
usuario.muestra_datos()