from datetime import time
from random import random

from Personaje import Personaje
from tecnica import tecnica


class Pokemon:

    def __init__(self):
        self.personajes = []
        self.personajeJugador = Personaje
        self.personajeCPU = Personaje

    def PersonajePokemon(self):

        tecnica1 = tecnica("Ascuas", 15, 15)
        tecnica2 = tecnica("Burbuja", 15, 15)
        tecnica3 = tecnica("Placaje", 15, 15)
        tecnica4 = tecnica("Psiquico", 35, 10)
        tecnica5 = tecnica("Latigo cepa", 15, 15)
        tecnica6 = tecnica("Pantalla humo", 0, 15)
        tecnica7 = tecnica("Mordisco", 15, 15)
        tecnica8 = tecnica("Pantalla luz", 0, 15)
        tecnica9 = tecnica("Arañazo", 10, 35)
        tecnica10 = tecnica("Rayo solar", 75, 5)
        tecnica11 = tecnica("Llamarada", 75, 5)
        tecnica12 = tecnica("Hidrobomba", 75, 5)
        tecnica13 = tecnica("Premonicion", 50, 15)
        tecnica14 = tecnica("Rayo hielo", 35, 15)
        tecnica15 = tecnica("Foco resplandor", 25, 10)
        tecnica16 = tecnica("Rayo", 35, 15)
        tecnica17 = tecnica("Trueno", 25, 10)
        tecnica18 = tecnica("Cola ferrea", 40, 15)
        tecnica19 = tecnica("Ataque arena", 0, 15)

        pokemon1 = Personaje("Charmander", "fuego", "audaz", 100, tecnica1, tecnica11, tecnica3, tecnica6)
        pokemon2 = Personaje("Squirtle", "agua", "timido", 100, tecnica12, tecnica2, tecnica3, tecnica7)
        pokemon3 = Personaje("Bulbasaur", "planta", "audaz", 100, tecnica5, tecnica10, tecnica9, tecnica15)
        pokemon4 = Personaje("Pikachu", "electrico", "timido", 100, tecnica16, tecnica17, tecnica18, tecnica3)
        pokemon5 = Personaje("Eevee", "Normal", "Valiente", 100, tecnica3, tecnica18, tecnica19, tecnica10)
        pokemon6 = Personaje("Mewtwo", "Psiquico", "timido", 100, tecnica13, tecnica14, tecnica8, tecnica4)

        self.personajes = [
            pokemon1 , pokemon2 , pokemon3 , pokemon4 , pokemon5 , pokemon6
        ]


        def listarPersonajes(self):
            print("**Personajes Disponibles**")
            for x in range(0, len(self.personajes)):
                print(self.personajes[x])

        def elegirPersonajeJugador(self):
            contador = 0
            salir = True
            personajeElegido = input("Personaje a elegir: ")
            while salir:
                if personajeElegido == self.personajes[contador].getNom():
                    self.personajeJugador = self.personajes[contador]
                    del self.personajes[contador]
                    salir = False

                contador += 1

            print("Jugador elegido por el Usuario: " + str(self.personajeJugador))

        def elegirPersonajeCPU(self):
            personajeAleatorio = random.choice(self.personajes)
            self.personajeCPU = personajeAleatorio
            self.personajes.remove(personajeAleatorio)
            print("Jugador elegido por la CPU: " + str(self.personajeCPU))

        def bajarVidaCPU(self, tecnica):
            if self.personajeCPU.getEscudo() == 0:
                self.personajeCPU.setVida(self.personajeCPU.getVida() - tecnica.getDano())
            else:
                self.personajeCPU.setEscudo(self.personajeCPU.getEscudo() - tecnica.getDano())

        def bajarVidaJugador(self, tecnica):
            if self.personajeJugador.getEscudo() == 0:
                self.personajeJugador.setVida(self.personajeJugador.getVida() - tecnica.getDano())
            else:
                self.personajeJugador.setEscudo(self.personajeJugador.getEscudo() - tecnica.getDano())

        def turnoJugador(self):
            print("Comienza el turno del Usuario...")
            time.sleep(3)
            print("Tecnicas del Personaje: " + "\n" + self.personajeJugador.getTecnica(1) + "\n"
                  + self.personajeJugador.getTecnica(2) + "\n" + self.personajeJugador.getTecnica(3))
            tecnicaEscogida = int(input("¿Qué tecnica querrías usar? "))
            self.bajarVidaCPU(self.personajeJugador.getTecnica(tecnicaEscogida))

        def jugar(self):
            # while self.personajeJugador.getVida() > 0 or self.personajeCPU.getVida() > 0:
            print(str(self.personajeJugador) + " " + str(self.personajeJugador.getVida()) + " ***VS*** " + str(
                self.personajeCPU) + " " + str(self.personajeCPU.getVida()))