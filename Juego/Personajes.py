class Personajes :

    def __int__(self):
        pass

    def __init__(self , nombre , tipo , habilidad , vida , tecnica1 , tecnica2 , tecnica3 , tecnica4):
        self.nombre=nombre
        self.tipo=tipo
        self.habilidad = habilidad
        self.vida = vida
        self.tecnicas = [tecnica1 , tecnica2 , tecnica3 , tecnica4]


    def RellenoArray(self,tecnica):
        self.tecnicas.append(tecnica)

    def getNombre(self):
        return self.nombre

    def getTipo(self):
        return self.tipo


    def getVida(self):
        return self.vida

    def getHabilidad(self):
        return self.habilidad

    def setNombre(self, nombre):
        self.nombre = nombre

    def setTipo(self, tipo):
        self.tipo = tipo

    def setHabilidad(self, habilidad):
        self.habilidad = habilidad

    def setVida(self, vida):
        self.vida = vida

    def Muestra(self):
        return "Tipo: " + self.tipo + "Habilidad: " + self.habilidad + "Vida: "+ self.vida + "Tecnicas: " + str[self.tecnicas[0],self.tecnicas[1],self.tecnicas[2],self.tecnicas[3]]

    def __str__(self):
        return self.nombre