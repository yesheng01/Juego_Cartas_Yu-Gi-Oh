from Usuario import Usuari

class Puja:

    def __init__(self, Usuario, CantidadOfrecida):
        self.Usuario = Usuario
        self.CantidadOfrecida = CantidadOfrecida

    def getUsuari(self):
        return self.Usuario

    def getCantidadOfrecida(self):
        return self.CantidadOfrecida

    def __str__(self):
        return "\n*********************************************\n" \
               "Informacion del que se ha pujado:" \
               "\nNombre: " + self.getUsuari().getNombre() + \
               "\nCantidad que  se ha pujado: " + str(
            self.getCantidadOfrecida()) + "\n******************************************\n"
