# Create the class
import random

import pokemon as pokemon

from Tecnica import Moves

class Pokemon:
    def __init__(self, name, types, moves, EVs, health='==================='):
        # save variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20 # Amount of health bars

def create():
        types = []

        for i in range(len(pokemon['types'])):
            types.append(pokemon['types'][i]['type']['name'])

    # Array of moves, gets 4 random moves on the pokemon selected

        moves = []
        for i in range(4):
            for k in range(len(pokemon['moves'])):
                rand = random.randrange(len(pokemon['moves']))
                if pokemon['moves'][rand]['move']['name'] not in moves:
                    new_move = Moves.create_mov(pokemon, rand)
                    moves.append(new_move)
                    break


