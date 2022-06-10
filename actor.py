from pyray import *


class Actor:
    def __init__(self):
        self._position_y = 0
        self._position_x = 0
        self._color = RED
        self._font_size = 20
        self._tag = ''

    def get_tag(self):
        return self._tag

    def get_font_size(self):
        return self._font_size

    def get_color(self):
        return self._color

    def get_pos_x(self):
        return self._position_x

    def get_pos_y(self):
        return self._position_y

    def set_pos_x(self, x):
        self._position_x = x

    def set_pos_y(self, y):
        self._position_y = y

    def set_color(self, color):
        self._color = color

    def set_tag(self, tag):
        self._tag = tag

    def set_font_size(self, size):
        self._font_size = size

    def show(self):
        draw_text(self._tag, self._position_x, self._position_y, self._font_size, self._color)
