import random import randrange
from pyray import *


from player import Player
from screen import Screen
from artifact import Artifact
from gem import Gem
from color import Color


def generateGems():
    gems = []
    for x in range(15):
        gem = Gem(Color())
        gem.set_tags('*')
        gem.set_pos_y(randrange(5, 40) * 5)
        gem.set_pos_x(randrange(5, 75) * 5)
        gems.append(gem)
    return gems

def generateRocks():
    rocks = []
    for x in range(15):
        rock = Rock()
        rock.set_tag('0')
        rock.set_pos_y(randrange(5, 40) * 5)
        rock.set_pos_x(randrange(5, 75) * 5)
        rock.set_color(Color())
        rocks.append(rock)
    return rocks

class Game:
    def __init__(self):
        self._player = Player()
        self._screen = Screen(800, 450)
        self._gems = generateGems()
        self.rocks = generateRocks()

