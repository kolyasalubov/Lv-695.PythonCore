print('''Welcome in the calculator of areas !!!
This program helps you find area of
rectangle, triangle and circle. ''')

def area_of_rectangle(lenght,width):
     return (lenght * width)

rectangle = area_of_rectangle

def area_of_triangle(a,b,c):
    p = (a + b + c) / 2
    return (round((p * (p - a) * (p - b) * (p - c)) ** 0.5,2))

triangle = area_of_triangle

def area_of_circle(r):
     from math import pi,pow
     return (round(pi * pow(r,2),2))

circle = area_of_circle

def main_func(choice):
     if choice == 'rectangle':
          a = int(input('Enter the width of the rectangle in cm\n'))
          b = int(input('Enter the length of the rectangle in cm\n'))
          print(f'The area of the rectangle is {area_of_rectangle(a, b)} cm.')
     elif choice == 'triangle':
          a = float(input('Enter the side "a" of the triangle in cm\n'))
          b = float(input('Enter the side "b" of the triangle in cm\n'))
          c = float(input('Enter the side "c" of the triangle in cm\n'))
          print(f'The area of triangle is {area_of_triangle(a, b, c)}.')
     elif choice == 'circle':
          r = int(input('Enter the radius of the circle in cm\n'))
          print(f'The area of the circle is {area_of_circle(r)} cm.')

choice = main_func(input('Please choose a figure: '))