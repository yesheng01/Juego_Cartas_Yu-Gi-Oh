class Tecnicas:
    def __init__(self , nombre , daño , contador):
        self.nombre=nombre
        self.daño = daño
        self.contador = contador

    def __str__(self):
        return self.nombre + "," + (self.daño) + "," + (self.contador)