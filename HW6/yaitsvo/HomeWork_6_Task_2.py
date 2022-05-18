def rectangle_area(width, length):
    return width * length


def triangle_area(a, b, c):
    p = 0.5 * (a + b + c)
    if (a+b) < c or (a+c) < b or (b+c) < a:
        print('There is no such triangle!')
    else:
        print('The area of the triangle is', (p * (p - a) * (p - b) * (p - c)) ** 0.5, 'cm')


def circle_area(r):
    from math import pi
    return pi * (r) ** 2


print('This program calculates the area of a figure if all its sides are found')
ent = input('Enter "r" - if you want to calculate the area of a rectangle\n'
            'Enter "t" - if you want to calculate the area of a triangle\n'
            'Enter "c" - if you want to calculate the area of a circle\n')
if ent.lower() == 'r':
    a = int(input('Enter the width of the rectangle in cm\n'))
    b = int(input('Enter the length of the rectangle in cm\n'))
    print(f'The area of the rectangle is {rectangle_area(a, b)} cm')
elif ent.lower() == 't':
    a = float(input('Enter the side "a" of the triangle in cm\n'))
    b = float(input('Enter the side "b" of the triangle in cm\n'))
    c = float(input('Enter the side "c" of the triangle in cm\n'))
    triangle_area(a, b, c)
elif ent.lower() == 'c':
    a = int(input('enter the radius of the circle in cm\n'))
    print(f'The area of the circle is {circle_area(a)} cm')