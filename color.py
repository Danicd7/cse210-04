class Color:
    def __init__(self, red, green, blue, alpha = 255):
        self._red = red
        self._green = green
        self._blue = blue
        self.alpha = alpha
    
    def to_tuple(self):

        return (self._red, self._green, self._red, self._blue, self._alpha)

# def Color():
#     colors = [RED, VIOLET, SKYBLUE, MAGENTA, BROWN]
#     return colors[range(0, 5)]k