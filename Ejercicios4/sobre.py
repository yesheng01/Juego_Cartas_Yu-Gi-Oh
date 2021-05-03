from datetime import datetime


class sobre:
    def __init__(self ,Nombre, Descripcion , Precio ):
        self.Identificador = datetime.now()
        self.Nombre = Nombre
        self.Descripcion = Descripcion
        self.Precio = Precio
        self.cartas = []

    def ObtenerCartas(self , carta):
        self.cartas.append(carta)


    def VeureCartesSobre(self):
        for x in self.cartas:
            print("**************************************************************************")
            print(str(x.getNombre()) + ", " + str(x.getTipos()) + ", " + str(x.getRareza()))
            print("**************************************************************************")