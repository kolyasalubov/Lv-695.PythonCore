class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def input_sides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : "))
                      for i in range(self.n)]

    def disp_sides(self):
        for i in range(self.n):
            print("Side", i+1, "is", self.sides[i])


class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 2)

    def findArea(self):
        a, b = self.sides
        square = a * b
        print(f'The area of the rectangle is {square}')


r = Rectangle()
r.input_sides()
r.disp_sides()
r.findArea()
