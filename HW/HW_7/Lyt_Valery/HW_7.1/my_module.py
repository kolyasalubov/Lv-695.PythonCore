from math import pi
from math import pow


def area_of_rectangle(number_1, number_2):
    area = number_1 * number_2
    return area


def area_of_triangle(number_1, number_2, number_3):
    p = (number_1 + number_2 + number_3) / 2
    area = pow((p * (p - number_1) * (p - number_2) * (p - number_3)), 0.5)
    return area


def area_of_circle(number_1):
    area = pi * pow(number_1, 2)
    return area
