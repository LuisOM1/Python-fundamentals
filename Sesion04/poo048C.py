import poo048B

class UsuariosPlatinum(poo048B.UsuariosPremium):
    sorteos=25

    def muestra_datos(self):
        super().muestra_datos()
        print('Eres un usuario platinum plus')

user=UsuariosPlatinum(33,'Mosquetero','Aramis','Cruz',25,700)
user.muestra_datos()