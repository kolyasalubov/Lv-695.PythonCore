class Polygon():

    def __init__(self, no_of_sides) -> None:
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    
    def inputSides(self) -> None:
        self.sides = [float(input(f'Enter side {i + 1}: ')) for i in range(self.n)]


class Rectangle(Polygon):
    """
    Rectangle area calculation Class
    """

    def __init__(self) -> None:
        super().__init__(2)
    
    def findAreaRectangle(self) -> None:
        a, b = self.sides
        area = a * b
        print('\n========== Result ==========')
        print(f'The area of the rectangle is {area}')

class Square(Polygon):
    """
    Square area calculation Class
    """

    def __init__(self) -> None:
        super().__init__(1)
    
    def findAreaSquare(self) -> None:
        area = self.sides[0] * self.sides[0]
        print('\n========== Result ==========')
        print(f'The area of the square is {area}')

print('Press "R" button - to calculate rectangle area.')
print('Press "S" button - to calculate square area.')  
print('Press "E" button - to exit.')
user_choice = input('Please choice what do you want to calculate: ').upper()

while user_choice not in ('R', 'S', 'E'):
    print('\n======== Attention =========')
    print('Only "R", "S" and "E" buttons are allowed.')
    user_choice = input('Please press a button again: ').upper()

match user_choice:
    case 'R':
        r = Rectangle()
        r.inputSides()
        r.findAreaRectangle()
    case 'S':
        s = Square()
        s.inputSides()
        s.findAreaSquare()
    case 'E':
        print('\nOk. See you later ;)')
