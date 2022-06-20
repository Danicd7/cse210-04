from random import randrange
from pyray import *

from gem import Gem
from player import Player
from rock import Rock
from screen import Screen


def colorize():
    colors = [RED, VIOLET, SKYBLUE, MAGENTA, BROWN]
    return colors[randrange(0, 5)]


def match(player, gems, rocks):
    for gem in gems:
        if player.get_pos_x() == gem.get_pos_x() and player.get_pos_y() == gem.get_pos_y():
            # print('got match')

            # remove gem
            gems.remove(gem)

            # generate another gem
            new_gem = Gem(colorize())
            new_gem.set_tag('*')
            new_gem.set_pos_y(randrange(5, 40)*5)
            new_gem.set_pos_x(randrange(5, 75)*5)
            gems.append(new_gem)
            return 'gem'

    for rock in rocks:
        if player.get_pos_x() == rock.get_pos_x() and player.get_pos_y() == rock.get_pos_y():
            # print('got match')

            # remove rock
            rocks.remove(rock)

            # generate another rock
            new_rock = Gem(colorize())
            new_rock.set_tag('*')
            new_rock.set_pos_y(randrange(5, 40)*5)
            new_rock.set_pos_x(randrange(5, 75)*5)
            gems.append(new_rock)
            return 'rock'


def generateGems():
    gems = []
    for x in range(15):
        gem = Gem(colorize())
        gem.set_tag('*')
        gem.set_pos_y(randrange(5, 40)*5)
        gem.set_pos_x(randrange(5, 75)*5)
        gems.append(gem)
    return gems


def generateRocks():
    rocks = []
    for x in range(15):
        rock = Rock()
        rock.set_tag('O')
        rock.set_pos_y(randrange(5, 40)*5)
        rock.set_pos_x(randrange(5, 75)*5)
        rock.set_color(colorize())
        rocks.append(rock)
    return rocks


class Game:
    def __init__(self):
        self._screen = Screen(800, 450)
        self._player = Player()
        self._gems = generateGems()
        self._rocks = generateRocks()

    def start_game(self):
        init_window(self._screen.getX(), self._screen.getY(), "Greedy")
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

            if is_key_down(KEY_DOWN):
                self._player.set_pos_y(self._player.get_pos_y() + 5)
                artifact = match(self._player, self._gems, self._rocks)
                if artifact == 'gem':
                    score += 20
                    continue
                elif artifact == 'rock':
                    score -= 50
                    continue
            if is_key_down(KEY_UP):
                self._player.set_pos_y(self._player.get_pos_y() - 5)
                artifact = match(self._player, self._gems, self._rocks)
                if artifact == 'gem':
                    score += 20
                    continue
                elif artifact == 'rock':
                    score -= 50
                    continue
            if is_key_down(KEY_RIGHT):
                self._player.set_pos_x(self._player.get_pos_x() + 5)
                artifact = match(self._player, self._gems, self._rocks)
                if artifact == 'gem':
                    score += 20
                    continue
                elif artifact == 'rock':
                    score -= 50
                    continue
            if is_key_down(KEY_LEFT):
                self._player.set_pos_x(self._player.get_pos_x() - 5)
                artifact = match(self._player, self._gems, self._rocks)
                if artifact == 'gem':
                    score += 20
                    continue
                elif artifact == 'rock':
                    score -= 50
                    continue

        close_window()
