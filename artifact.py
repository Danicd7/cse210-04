from actor import Actor

class Artifact(Actor):
    def __init__(self):
        super().__init__()
        self._value = 0
        self._name = 'artifact'

    def get_value(self):
        return self._value

    def get_name(self):
        return self._name

    def set_value(self, value):
        self._value = value

    def set_name(self, name):
        self._value = name
