from random import random

from numpy import array

from Personajes import Personajes
from Tecnicas import Tecnicas


class Pokemon:

    def __init__(self):
        self.personajes = []

    def PersonajePokemon(self):

        tecnica1 = Tecnicas("Ascuas", 15, 15)
        tecnica2 = Tecnicas("Burbuja", 15, 15)
        tecnica3 = Tecnicas("Placaje", 15, 15)
        tecnica4 = Tecnicas("Psiquico", 35, 10)
        tecnica5 = Tecnicas("Latigo cepa", 15, 15)
        tecnica6 = Tecnicas("Pantalla humo", 0, 15)
        tecnica7 = Tecnicas("Mordisco", 15, 15)
        tecnica8 = Tecnicas("Pantalla luz", 0, 15)
        tecnica9 = Tecnicas("Arañazo", 10, 35)
        tecnica10 = Tecnicas("Rayo solar", 75, 5)
        tecnica11 = Tecnicas("Llamarada", 75, 5)
        tecnica12 = Tecnicas("Hidrobomba", 75, 5)
        tecnica13 = Tecnicas("Premonicion", 50, 15)
        tecnica14 = Tecnicas("Rayo hielo", 35, 15)
        tecnica15 = Tecnicas("Foco resplandor", 25, 10)
        tecnica16 = Tecnicas("Rayo", 35, 15)
        tecnica17 = Tecnicas("Trueno", 25, 10)
        tecnica18 = Tecnicas("Cola ferrea", 40, 15)
        tecnica19 = Tecnicas("Ataque arena", 0, 15)

        pokemon1 = Personajes("Charmander", "fuego", "audaz", 100, tecnica1, tecnica11, tecnica3, tecnica6)
        pokemon2 = Personajes("Squirtle", "agua", "timido", 100, tecnica12, tecnica2, tecnica3, tecnica7)
        pokemon3 = Personajes("Bulbasaur", "planta", "audaz", 100, tecnica5, tecnica10, tecnica9, tecnica15)
        pokemon4 = Personajes("Pikachu", "electrico", "timido", 100, tecnica16, tecnica17, tecnica18, tecnica3)
        pokemon5 = Personajes("Eevee", "Normal", "Valiente", 100, tecnica3, tecnica18, tecnica19, tecnica10)
        pokemon6 = Personajes("Mewtwo", "Psiquico", "timido", 100, tecnica13, tecnica14, tecnica8, tecnica4)

        a = array([pokemon1 , pokemon2 , pokemon3 , pokemon4 , pokemon5 ,pokemon6])

        Personajes.Muestra(a)