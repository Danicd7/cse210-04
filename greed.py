import random 

from player import Player
from screen import Screen
from artifact import Artifact

class Game:
    def __init__(self):
        self._player = Player()
        self._screen = Screen()
        self._artifact = Artifact()

    def get_player(self):
        return self._player
    
    def set_player(self, player):
        self._player = player

