import math

def areaOfRectangle(length_of_rectangle: float, width_of_rectangle: float) ->float:
    """The function returns the area of rectangle."""

    return round(length_of_rectangle*width_of_rectangle,2)

def areaOfTriangle(side_of_triangle_1: float, side_of_triangle_2: float, angle_of_triangle: float) ->float:
    """The function returns the area of triangle."""

    return round(0.5*side_of_triangle_1*side_of_triangle_2*math.sin(math.radians(angle_of_triangle)),2)

def areaOfCircle(radius_of_circle: float) ->float:
    """The function returns the area of circle."""

    return round(math.pi*(radius_of_circle**2),2)

key=True
while key:
    geom_figure=int(input("Select the geometric figure: rectangle enter 1, triangle enter 2, circle enter 3: "))
    if geom_figure==1:
        key=False
        length_of_rectangle=float(input("Set the length of the rectangle (in cm): "))
        width_of_rectangle=float(input("Set the width of the rectangle (in cm): "))
        print(f"The area of the rectangle is {areaOfRectangle(length_of_rectangle,width_of_rectangle)} sq.cm.")
    elif geom_figure==2:
        key=False
        side_of_triangle_1=float(input("Set the first side of the triangle (in cm): "))
        side_of_triangle_2=float(input("Set the second side of the triangle (in cm): "))
        angle_of_triangle=int(input("Set the angle between the specified sides of the triangle (in degrees): "))
        print(f"The area of the triangle is {areaOfTriangle(side_of_triangle_1,side_of_triangle_2,angle_of_triangle)} sq.cm.")
    elif geom_figure==3:
        key=False
        radius_of_circle=float(input("Set the radius of the circle (in cm): "))
        print(f"The area of the circle is {areaOfCircle(radius_of_circle)} sq.cm.")
    else:
        key=True
        print("Data format error!")
