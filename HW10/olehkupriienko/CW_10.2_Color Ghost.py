class Ghost(object):

    def __init__(self):
        colors = ["white", "yellow", "purple", "red"]
        from random import choice
        self.color = choice(colors)


# Test
ghosts = [Ghost().color for _ in range(10)]
print(*ghosts)
