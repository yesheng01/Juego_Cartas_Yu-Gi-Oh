from Puja import Puja
from Usuario import Usuari


class Subasta:
    def __init__(self, NombreProducto, UsuarioPropietario):
        self.NombreProducto = NombreProducto
        self.UsuarioPropietario = UsuarioPropietario
        self.Situacion = True
        self.pujas = [Puja(Usuari, 0)]
        self.pujasamajor = Puja(Usuari, 0)

    def setNombreProducto(self, NombreProducto):
        self.NombreProducto = NombreProducto

    def getNombreProducto(self):
        return self.NombreProducto

    def getUsuarioPropietario(self):
        return self.UsuarioPropietario

    def getPujasaMayor(self):
        return self.pujasamajor

    def setPujasaMajor(self, PujasaMayot):
        self.pujasamajor = PujasaMayot

    def getPujas(self):
        return self.pujas

    def getEstadoSubasta(self):
        return self.Situacion

    def setEstadoSubasta(self, estado):
        self.Situacion = estado

    def historial(self):
        for puja in self.pujas[1::]:
            yield puja.__str__()

    def getHistorial(self):

        message ="************************************************\nHistorial de pujadores del objeto " + \
                 self.getNombreProducto()
        for historial in self.historial():
             message += historial
        return message

    def Pujar(self, Usuario, dinero):
        if self.Situacion != Usuario.getDinero() > dinero:
                if Usuario.getNombre() != self.UsuarioPropietario:
                    if dinero > self.getPujasaMayor().getCantidadOfrecida():
                        puja = Puja(Usuario, dinero)
                        self.setPujasaMajor(puja)
                        self.pujas.append(puja)
                        return "Puja Aceptada\n"
                    else:
                        return "No se pudo realizar la puja , debe introducir una cantidad mas alta \n"
                else:
                    return False
        else:
            return "Aceptada \n"

    def PujarUsuario(self, Usuario):
        if self.pujasamajor == Puja:
            if Usuario.getDinero() > self.pujasamajor:
                puja = Puja(Usuario, self.pujasamajor.getCantidadOfrecida() + 1)
                self.setPujasaMajor(puja)
                self.pujas.append(puja)
            else:
                return "Puja \n"
        else:
            puja = Puja(Usuario, 1)
            self.setPujasaMajor(puja)
            self.pujas.append(puja)
            return "Pujada \n"

    def Comprobar(self):
        if self.getEstadoSubasta():
            return "La subasta se ha abierto."
        else:
            return "La subasta se ha cerrado."

    def Ejecutar(self):

        if self.Comprobar():
            self.getUsuarioPropietario().incrementarCredito(self.getPujasaMayor().getCantidadOfrecida())
            self.getPujasaMayor().getUsuari().decrementarCredito(self.getPujasaMayor().getCantidadOfrecida())
            self.setEstadoSubasta(False)
            return "******************************************************\nSubasta finalizada correctamente.\n"
        else:
            return "***********************************************************\nLa subasta ya ha sido cerrada.\n"