import sys
import time

from Tecnica import Tecnica


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)

class Personaje:
    def __init__(self, nombre, vida, nivel):
        self.Nombre=nombre
        self.vida=vida
        self.Nivel=nivel
        self.Tecnicas=[]

    def getNombre(self):
        return self.Nombre

    def getVida(self):
        return self.vida

    def getNivel(self):
        return self.Nivel

    def getTecnica(self):
        conta=0
        for x in self.Tecnicas:
            conta=conta+1
            print(str(conta) + " - " + str(x.getNombre()))
    def getTecnica1(self, int):
        return self.Tecnicas[int]

    def setTecinas(self, Tecnica1, Tecnica2):
        self.Tecnicas.append(Tecnica1)
        self.Tecnicas.append(Tecnica2)

    def recibirDanoFisico(self, int):
            self.vida=self.vida-int


    def Datos_Personaje(self):
        delay_print("\n************************************************ \t"
                    "\nNombre  ==================================== " + self.Nombre+
                    "\nNivel   ************************************ " + str(self.Nivel)+
                    "\nVida    ==================================== " + str(self.vida)
                    )



