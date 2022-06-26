class Polygon:
    def __init__(self, sides):
        self.n = sides
        self.sides = [0 for _ in range(sides)]

    def inputSides(self):
        self.sides = [float(input(f"Enter side {str(i+1)}:\n"))
                      for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print(f"Side {i+1} is {self.sides[i]}")


class Square(Polygon):
    def __init__(self):
        super().__init__(1)

    def findArea(self):
        a = self.sides[0]
        area = a ** 2
        print(f"The area of square is {area}")


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)

    def findArea(self):
        a = self.sides[0]
        b = self.sides[1]
        area = a * b
        print(f"The area of rectangle is {area}")


sq = Square()
sq.inputSides()
sq.dispSides()
sq.findArea()

r = Rectangle()
r.inputSides()
r.dispSides()
r.findArea()