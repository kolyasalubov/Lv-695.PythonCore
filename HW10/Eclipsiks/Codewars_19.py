import random

class Ghost:

    def __init__(self):
        color_range = ["white", "yellow", "purple", "red"]
        self.color = random.choice(color_range)