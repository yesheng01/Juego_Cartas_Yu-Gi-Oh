class Tecnica:
    def __init__(self, Nombre, dano):
        self.Nombre=Nombre
        self.danoFisico=dano
    def getNombre(self):
            return self.Nombre
    def getDanoFisico(self):
            return int(self.danoFisico)