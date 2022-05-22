import random
class Ghost(object):
    def __init__(self):
        self.color = random.choice(['white', 'yellow', 'red', 'purple'])


ghost = Ghost()
print(ghost.color)