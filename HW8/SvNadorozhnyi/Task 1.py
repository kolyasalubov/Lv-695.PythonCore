class Polygon:
    def __init__(self, number_of_sides):
        self.n = number_of_sides
        self.sides = [0 for i in range(number_of_sides)]

    def inputSides(self):
        if self.n == 2:
            self.sides = [float(input(f"Enter {str(i + 1)} side of rectangle: ")) for i in range(self.n)]
        elif self.n == 3:
            self.sides = [float(input(f"Enter {str(i + 1)} side of triangle: ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print(f"Side {i + 1}, is {self.sides[i]}")


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)

    def area(self):
        height, width = self.sides
        area_of_rectangle = height * width
        return f"Area of rectangle = {area_of_rectangle}"


class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)

    def area(self):
        first_side, second_side, third_side = self.sides
        p = (first_side + second_side + third_side) / 2
        area_of_triangle = (p * (p - first_side) * (p - second_side) * (p - third_side)) ** 0.5
        return f"Area of triangle = {area_of_triangle}"


rectangle = Rectangle()
rectangle.inputSides()
rectangle.dispSides()
print(rectangle.area())
triangle = Triangle()
triangle.inputSides()
triangle.dispSides()
print(triangle.area())
