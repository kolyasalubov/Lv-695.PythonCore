from math import pow
from math import pi


def area_rectangle(a: float, b: float) -> float:
    """
    Function calculates area of rectangle
    Args:
        a (float): height of rectangle
        b (float): length of rectangle

    Returns:
        float: area of rectangle
    """

    return a * b

def area_triangle(h: float, a: float) -> float:
    """
    Function calculates area of triangle
    Args:
        h (float): height of triangle
        a (float): side of triangle

    Returns:
        float: area of triangle
    """    

    return a * h * 0.5

def area_circle(r: float) -> float:
    """
    Function calculates area of circle
    Args:
        r (float): radius of circle

    Returns:
        float: area of circle
    """    
    return pi * pow(r, 2)

