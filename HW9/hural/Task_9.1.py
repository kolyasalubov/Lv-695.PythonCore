
class Rectangle(Polygon):

    def __init__(self, lenghts_of_sides):
        Polygon.__init__(self, 4)
        self.lengths_of_sides = lengths_of_sides  # list of two numbers

    def get_area(self):
        '''return the area of the rectangle: length x width'''
        x, y = self.lenghts_of_sides
        return x * y

class Triangle(Polygon):

    def __init__(self, lengths_of_sides):
        Polygon.__init__(self, 3)
        self.lengths_of_sides = lengths_of_sides  # list of three numbers

    def get_area(self):
        '''return the area of the triangle using the semi-perimeter method'''
        a, b, c = self.lengths_of_sides

        # calculate the semi-perimeter
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5