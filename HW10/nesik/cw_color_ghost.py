import random


class Ghost():
    colors = ["white", "yellow", "purple", "gold"]

    def __init__(self):
        self.color = random.choice(Ghost.colors)
