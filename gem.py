from artifact import Artifact


class Gem(Artifact):
    def __init__(self, color):
        super().__init__()
        self.set_color(color)
