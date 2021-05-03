from tecnica import tecnica


class Personaje:

    def __int__(self):
        pass

    def __init__(self, nom, tipus, habilidad, vida, tecnica1, tecnica2, tecnica3 , tecnica4):
        self.nom = nom
        self.habilidad = habilidad
        self.tipus = tipus
        self.vida = vida
        self.tecnicas = [tecnica1, tecnica2, tecnica3,tecnica4]

    def rellenarArray(self, Tecnica):
        self.tecnicas.append(Tecnica)

    def detalles(self):
        return "Tipo: " + self.tipus + "\nAtaque: " + str(self.atac) + \
               "\nVida: " + str(self.vida) + "\nTecnicas{\n\t[" + \
               str(self.tecnicas[0]) + "]\n\t[" + str(self.tecnicas[1]) + \
               "]\n\t[" + str(self.tecnicas[2]) + "]\n\t}" + "]\n\t[" + str(self.tecnicas[3]) + "]\n\t}"

    def getNom(self):
        return self.nom

    def getTipus(self):
        return self.tipus

    def getAtac(self):
        return self.atac

    def getVida(self):
        return self.vida

    def getTecnica(self,num):
        return self.tecnicas[num-1]

    def setNom(self, nom):
        self.nom = nom

    def setTipus(self, tipus):
        self.tipus = tipus

    def setAtac(self, atac):
        self.atac = atac

    def setVida(self, vida):
        self.vida = vida



    def __str__(self):
        return self.nom