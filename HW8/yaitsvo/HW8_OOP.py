class Polygon:
    def __init__(self, num_of_sides):
        self.sides = None
        self.num = num_of_sides



class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 2)

    def rectangle_area(self):
        self.sides = [float(input(f'Enter side {i} of figure in cm ')) for i in range(1, self.num + 1)]
        a, b = self.sides
        print(f'The area of rectangle is {a * b} cm')

rect = Rectangle()
rect.rectangle_area()