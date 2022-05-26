import math

def areaOfRectangle(length_of_rectangle: float, width_of_rectangle: float) ->float:
    """The function returns the area of rectangle."""

    return round(length_of_rectangle*width_of_rectangle,2)

def areaOfTriangle(side_of_triangle: float, height_of_triangle: float) ->float:
    """The function returns the area of triangle."""

    return round(0.5*side_of_triangle*height_of_triangle,2)

def areaOfCircle(radius_of_circle: float) ->float:
    """The function returns the area of circle."""

    return round(math.pi*math.pow(radius_of_circle,2),2)
    