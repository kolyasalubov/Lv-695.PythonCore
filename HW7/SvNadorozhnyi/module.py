import math


def area_of_triangle(height, base):
    area = 0.5 * height * base
    return area


def area_of_rectangle(height, width):
    area = height * width
    return area


def area_of_circle(radius):
    area = math.pi * math.pow(radius, 2)
    return area

