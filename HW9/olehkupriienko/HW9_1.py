"""Create a polygon class and a rectangle class
that inherits from the polygon class and finds the square of rectangle."""


class Polygon:
    def __init__(self, num_of_sides):
        self.num_of_sides = num_of_sides
        # self.sides = [0 for i in range(self.num_of_sides)]
        # я відразу виконав введення значень сторін, щоб не призначати їм нульові значення
        self.set_sides()

    def set_sides(self):
        # тут вводимо значення сторін
        self.sides = [float(input(f'Ender value of side {i+1}: ')) for i in range(self.num_of_sides)]

    def disp_sides(self):
        for _ in range(self.num_of_sides):
            print(f'Side {_+1} is {self.sides[_]}')


class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)

    def find_triangle_square(self):
        x, y, z = self.sides
        p = (x + y + z) / 2
        square = (p * (p - x) * (p - y) * (p - z))**0.5
        print(f'The square of triangle is {square:.2f}')


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)

    def find_rectangle_square(self):
        x, y = self.sides
        square = x * y
        print(f'The square of rectangle is {square:.2f}')


my_rect = Rectangle()
my_rect.find_rectangle_square()

my_triangle = Triangle()
my_triangle.find_triangle_square()
