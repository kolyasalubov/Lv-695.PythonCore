import math
def areaOfRectangle(length_of_rectangle,width_of_rectangle):
    """The function returns the area of rectangle."""
    return round(length_of_rectangle*width_of_rectangle,2)
def areaOfTriangle(side_of_triangle_1,side_of_triangle_2,angle_of_triangle):
    """The function returns the area of triangle."""
    return round(0.5*side_of_triangle_1*side_of_triangle_2*math.sin(math.radians(angle_of_triangle)),2)
def areaOfCircle(radius_of_circle):
    """The function returns the area of circle."""
    return round(math.pi*(radius_of_circle**2),2)
key=True
while key:
    geom_figure=int(input("Select the geometric figure: rectangle enter 1, triangle enter 2, circle enter 3:"))
    if geom_figure==1:
        key=False
        length_of_rectangle=float(input("Set the length of the rectangle:"))
        width_of_rectangle=float(input("Set the width of the rectangle:"))
        print(f"The area of rectangle is {areaOfRectangle(length_of_rectangle,width_of_rectangle)}.")
    elif geom_figure==2:
        key=False
        side_of_triangle_1=float(input("Set the first side of the triangle:"))
        side_of_triangle_2=float(input("Set the second side of the triangle:"))
        angle_of_triangle=int(input("Set the angle in degrees between the specified sides of the triangle:"))
        print(f"The area of triangle is {areaOfTriangle(side_of_triangle_1,side_of_triangle_2,angle_of_triangle)}.")
    elif geom_figure==3:
        key=False
        radius_of_circle=float(input("Set the radius of the circle:"))
        print(f"The area of circle is {areaOfCircle(radius_of_circle)}.")
    else:
        key=True
        print("Data format error!")
