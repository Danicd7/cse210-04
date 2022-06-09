from actor import Actor


class Player(Actor):
    def __init__(self):
        super().__init__()
        self._name = 'player'