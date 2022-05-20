from math import pow
from math import pi


def rectangle_area():
    a = float(input('Enter the width of the rectangle in cm\n'))
    b = float(input('Enter the length of the rectangle in cm\n'))
    return print(f'The area of the rectangle is {round(a*b,2)} cm')


def triangle_area():
    a = float(input('Enter the side "a" of the triangle in cm\n'))
    b = float(input('Enter the side "b" of the triangle in cm\n'))
    c = float(input('Enter the side "c" of the triangle in cm\n'))
    p = 0.5 * (a + b + c)
    if (a+b) < c or (a+c) < b or (b+c) < a:
        print('There is no such triangle!')
    else:
        print('The area of the triangle is', round(((p * (p - a) * (p - b) * (p - c)) ** 0.5), 2), 'cm')


def circle_area():
    r = float(input('enter the radius of the circle in cm\n'))
    return print('The area of the circle is', round(pi * r ** 2, 2), 'cm')

