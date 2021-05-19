import random
import sys
import time

from numpy.random import randint

from Personaje import Personaje
from Tecnica import Tecnica


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)


class Juego:

    def __init__(self, nombre):
        self.nombre = nombre
        self.p1 = Personaje;
        self.t1 = Tecnica;
        self.t2 = Tecnica;
        self.p2 = Personaje;
        self.personajes = []
        self.jugador1 = Personaje;
        self.jugador2 = Personaje;

    def Personaje_Tecnica(self):

        self.p1 = Personaje("Obelisk", 2000, 30)
        self.t1 = Tecnica("Tumba", 1000)
        self.t2 = Tecnica("Golpe de Muerte", 500)

        self.p2 = Personaje("Ra", 2000, 30)
        self.t3 = Tecnica("Divinidad", 550)
        self.t4 = Tecnica("Rayo de Muerte", 1000)

        self.p3 = Personaje("Mago Oscuro", 2000, 30)
        self.t5 = Tecnica("Magia Oscura", 1500)
        self.t6 = Tecnica("Disparo", 950)

        self.personajes.append(self.p1)
        self.personajes.append(self.p2)
        self.personajes.append(self.p3)

        self.p1.setTecinas(self.t1, self.t2)
        self.p2.setTecinas(self.t3, self.t4)
        self.p3.setTecinas(self.t5, self.t6)

    def mostrar(self):
        delay_print("Yu-Gi-Oh\n")
        delay_print("Personajes: \n")
        print("------------")
        self.p1.Datos_Personaje()
        self.p2.Datos_Personaje()
        self.p3.Datos_Personaje()

    def Elegir_Personaje(self):
        j1 = input("\nJugador 1, seleccione un personaje: ")
        if j1 == "1":
            self.jugador1 = self.p1
        elif j1 == "2":
            self.jugador1 = self.p2
        elif j1 == "3":
            self.jugador1 = self.p3
        print("El jugador 1 ha seleccionado a: " + str(self.jugador1.getNombre()))

    def ElegirCPU(self):
        r = random.choice(range(1, 3))
        if r == 1:
            if self.jugador1 == self.p1:
                self.jugador2 = self.p3
            else:
                self.jugador2 = self.p1
        elif r == 2:
            if self.jugador1 == self.p2:
                self.jugador2 = self.p1
            else:
                self.jugador2 = self.p2
        elif r == 3:
            if self.jugador1 == self.p3:
                self.jugador2 = self.p2
            else:
                self.jugador2 = self.p3

        print("Ha elegido el siguiente monstruo: " + str(self.jugador2.getNombre()))

    def usarTecnica(self, jugador, enemigo):
        print("----------------------")
        print("Tecnicas de: " + jugador.getNombre())
        print(jugador.getTecnica())
        tec = input("Seleccione una tecnica: ")
        if tec == "1":
            if (jugador.getTecnica1(0).getDanoFisico()) > 0:
                enemigo.recibirDanoFisico(int(jugador.getTecnica1(0).getDanoFisico()))
                print("La tecnica es usado y es el siguiente : " + str(
                    jugador.getTecnica1(0).getNombre()) + " la vida de " + enemigo.getNombre() + " es: " + str(
                    enemigo.getVida()))

        elif tec == "2":
            if (jugador.getTecnica1(1).getDanoFisico()) > 0:
                enemigo.recibirDanoFisico(int(jugador.getTecnica1(1).getDanoFisico()))
                print("La tecnica es usado y es el siguiente : " + str(
                    jugador.getTecnica1(1).getNombre()) + " la vida de " + enemigo.getNombre() + " es: " + str(
                    enemigo.getVida()))

    def usarTecnicaCPU(self):

        q = randint(1, 2)
        print("----------------------")
        if q == 1:
            if (self.jugador2.getTecnica1(0).getDanoFisico()) > 0:
                self.jugador1.recibirDanoFisico(int(self.jugador2.getTecnica1(0).getDanoFisico()))
                print(self.jugador2.getNombre() + " el CPU utiliza:   " + self.jugador2.getTecnica1(0).getNombre())
            print("Tecnica realizada correctamente, la vida de " + self.jugador1.getNombre() + " es: " + str(
                self.jugador1.getVida()))

        elif q == 2:
            if (self.jugador2.getTecnica1(1).getDanoFisico()) > 0:
                self.jugador1.recibirDanoFisico(int(self.jugador2.getTecnica1(1).getDanoFisico()))
                print(self.jugador2.getNombre() + " el CPU utiliza: " + self.jugador2.getTecnica1(1).getNombre())
            print("Tecnica realizada correctamente, la vida de " + self.jugador1.getNombre() + " es : " + str(
                self.jugador1.getVida()))

    def lucha(self):
        print("*************************Empieza el juego**************************")
        rondas = 0;
        while self.jugador1.getVida() > 0 and self.jugador2.getVida() > 0:
            rondas = rondas + 1;
            print("------------")
            print("Ronda: " + str(rondas))
            print("-------------")
            self.usarTecnica(self.jugador1, self.jugador2)
            print("")
            if self.jugador2.getVida() > 0:
                self.usarTecnicaCPU()

        if self.jugador1.getVida() <= 0:
            print("\n-------------------------")
            print("Ha ganado:" + str(self.jugador2.getNombre()))
        else:
            print("\n-------------------------")
            print("Ha ganado:" + str(self.jugador1.getNombre()))

    def volverJugar(self):
        volverJuego = input("¿Deseas volver a jugar? [s/n]")
        if volverJuego == "s":
            return True
        elif volverJuego == "n":
            return False
        else:
            print("Opcion no valida, saliendo del juego...")
            return False
