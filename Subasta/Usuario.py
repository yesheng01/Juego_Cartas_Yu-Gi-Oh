class Usuari:
    def __init__(self, Nombre, Dinero):
        self.Nombre = Nombre
        self.Dinero = Dinero

    def incrementarCredito(self, Cantidad):
        self.Dinero += Cantidad

    def decrementarCredito(self, Cantidad):
        self.Dinero -= Cantidad

    def getNombre(self):
        return self.Nombre

    def getDinero(self):
        return self.Dinero

    def setDinero(self, Dinero):
        self.Dinero = Dinero

    def __str__(self):
        return self.getNombre()