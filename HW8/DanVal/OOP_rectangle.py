class Polygon:
    pass


class Rectangle:
    def __init__(self, height, length):
        self.height = height
        self.length = length

    def square(self):
        return self.height * self.length
