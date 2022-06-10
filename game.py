from random import randrange
from pyray import *


from player import Player
from screen import Screen
from artifact import Artifact
from gem import Gem
from rock import Rock
from color import Color

# def Color():
#     colors = [RED, VIOLET, SKYBLUE, MAGENTA, BROWN]
#     return colors[range(0, 5)]


def match(player, gems, rocks):
    for gem in gems:
        if player.get_pos_x() == gem.get_pos_x() and player.get_pos_y() == gem.get_pos_y():

            gems.remove(gem)

            new_gem = Gem(Color())
            new_gem.set_tag('*')
            new_gem.set_pos_y(randrange(5, 40) * 5)
            new_gem.set_pos_x(randrange(5, 75) * 5)
            gems.append(new_gem)
            return 'gem'
    for rock in rocks:
        if player.get_pos_x() == rock.get_pos_x() and player.get_pos_y() == rock.get_pos_y():
            
            rocks.remove(rock)

            new_rock = Gem(Color())
            new_rock.set_tag('0')
            new_rock.set_pos_y(randrange(5, 40) * 5)
            new_rock.set_pos_x(randrange(5, 75) * 5)
            gems.append(new_rock)
            return 'rock'

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

    def start_game(self):
        init_window(self._screen.getX(), self._screen.getY(), 'Greedy')
        set_target_fps(60)
        self._player.set_pos_x(400)
        self._player.set_pos_y(350)
        self._player.set_color(BLACK)
        self._player.set_tag('#')
        score = 0

        while not window_should_close():
            begin_drawing()
            clear_background(RAYWHITE)
            draw_text('YOUR SCORE: ' + str(score), 0, 0, 28, BLACK)
            
            for gem in self._gems:
                gem.show()

            for rock in self._rocks:
                rock.show()
            
            self._player.show()
            end_drawing()

            if is_key_down(KeyboardKey.KEY_DOWN):
                self.player.set_pos_y(self._player.get_pos_y() + 5)
                artifact = match(self._player, self._gems, self._rocks)
                if artifact == 'gem':
                    score += 20
                    continue
                elif artifact == 'rock':
                    score -= 50
                    continue
            
            if is_key_down(KeyboardKey.KEY_UP):
                self.player.set_pos_y(self._player.get_pos_y() + 5)
                artifact = match(self._player, self._gems, self._rocks)
                if artifact == 'gem':
                    score += 20
                    continue
                elif artifact == 'rock':
                    score -= 50
                    continue
            
            if is_key_down(KeyboardKey.KEY_RIGHT):
                self.player.set_pos_x(self._player.get_pos_x() + 5)
                artifact = match(self._player, self._gems, self._rocks)
                if artifact == 'gem':
                    score += 20
                    continue
                elif artifact == 'rock':
                    score -= 50
                    continue
            
            if is_key_down(KeyboardKey.KEY_LEFT):
                self.player.set_pos_x(self._player.get_pos_x() + 5)
                artifact = match(self._player, self._gems, self._rocks)
                if artifact == 'gem':
                    score += 20
                    continue
                elif artifact == 'rock':
                    score -= 50
                    continue

        close_window()