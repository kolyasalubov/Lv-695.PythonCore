import Calc_square

key=True
while key:
    geom_figure=int(input("Select the geometric figure: rectangle enter 1, triangle enter 2, circle enter 3: "))
    if geom_figure==1:
        key=False
        length_of_rectangle=float(input("Set the length of the rectangle (in cm): "))
        width_of_rectangle=float(input("Set the width of the rectangle (in cm): "))
        print(f"The area of the rectangle is {Calc_square.areaOfRectangle(length_of_rectangle,width_of_rectangle)} sq.cm.")
    elif geom_figure==2:
        key=False
        side_of_triangle=float(input("Set the base side of the triangle (in cm): "))
        height_of_triangle=float(input("Set the height of the triangle (in cm): "))
        print(f"The area of the triangle is {Calc_square.areaOfTriangle(side_of_triangle,height_of_triangle)} sq.cm.")
    elif geom_figure==3:
        key=False
        radius_of_circle=float(input("Set the radius of the circle (in cm): "))
        print(f"The area of the circle is {Calc_square.areaOfCircle(radius_of_circle)} sq.cm.")
    else:
        key=True
        print("Data format error!")
        