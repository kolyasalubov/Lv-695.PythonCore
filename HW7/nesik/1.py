from area_calc import *

print('Enter "C" - to calculate circle area')
print('Enter "T" - to calculate triangle area')
print('Enter "R" - to calculate rectangle area')
print('Enter "E" - to exit')

choice = input('Please choice what do you want to calculate: ').upper().strip()

while choice not in ('C', 'E', 'C', 'R'):
    choice = input('Please enter the required: ').upper()

match choice:
    case 'R':
        AreaOfRectangle()
    case 'T':
        AreaOfTriangle()
    case 'C':
        AreaOfCircle()
    case 'E':
        exit
