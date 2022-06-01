class Poligon:
    def __init__(self, n_of_sides):
        self.n = n_of_sides
        self.sides = [0 for i in range(n_of_sides)]

    def inputSides(self):
        self.sides = [float(input(f"Enter side {str(i+1)}: ")) for i in range (self.n)]

    def dispSides(self):
        for i in range(self.n):
            print(f"Side {i+1} is {self.sides[i]}")


class Rectangle(Poligon):
    def __init__(self):
        super().__init__(2)

    def findAreaRectangle(self):
        a, b = self.sides
        area = a * b
        print(f"The area of the rectangle is {area}.")


class Triangle(Poligon):
    def __init__(self):
        super().__init__(3)

    def findArea(self):
        a, b, c = self.sides
        p = (a + b + c) / 2
        area = (p*(p-a)*(p-b)*(p-c)) ** 0.5
        print(f"The area of the triangle is {area}.")


class Square(Poligon):
    def __init__(self):
        super().__init__(1)

    def findAreaSquare(self):
        a = self.sides
        area = a ** 2
        print(f"The area of the triangle is {area}.")

r = Rectangle()
r.inputSides()
r.dispSides()
r.findAreaRectangle()

# s = Square()
# s.inputSides()
# s.findAreaSquare()
# s.dispSides()

# t = Triangle()
# t.inputSides()
# t.dispSides()
# t.findArea()

