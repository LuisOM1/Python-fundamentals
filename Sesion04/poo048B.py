
import poo048A

class UsuariosPremium(poo048A.Usuarios):
    def __init__(self, id,alias,nombre,apellidos,sorteos,puntos):
        super().__init__(id,alias,nombre,apellidos)
        self.sorteos=sorteos
        self.puntos=puntos
        self.contenido_premium=True

    def muestra_datos(self):
        super().muestra_datos()
        print(f'Tienes {self.puntos} puntos para canjear en premios')
        print(f'Tienes derecho a participar en: {self.sorteos} sorteos')

#creamos la instancia de un objeto de clase UsuariosPremium
persona=UsuariosPremium(21,'Empresario','Juan','Pérez',10,200)
persona.muestra_datos()
