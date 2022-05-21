from math import pi
from math import pow

def rectangle():
    rec_length = float(input("Type the length of the rectangle:\n"))
    rec_hight = float(input("Type the hight of the rectangle:\n"))
    return f"The area of your rectangle is: {rec_length * rec_hight}"

def triangle():
    tri_length = float(input("Type the length of basis of the triangle:\n"))
    tri_hight = float(input("Type the hight of the triangle:\n"))
    return f"The area of your triangle is: {(tri_length * tri_hight)/2}"

def circle():
    radius = float(input("Type the radius of the circle:\n"))
    ar = pow((radius * pi), 2)
    return f"The area of your triangle is: {float(ar)}"