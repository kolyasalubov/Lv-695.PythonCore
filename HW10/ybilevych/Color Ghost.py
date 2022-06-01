from random import choice

class Ghost:
    def __init__(self):
        color = ['white', 'yellow', 'purple', 'red']
        self.color = choice(color)
