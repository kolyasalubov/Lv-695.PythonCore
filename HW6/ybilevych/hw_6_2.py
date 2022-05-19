def area():
    """Func that calculates the area of a rectangle, triangle and circle, 
    depending on the user's choice"""
    x = input("Type a figure you want to calculate area: (rectangle, triangle or circle):\n")
    if x == "rectangle":
        rec_length = float(input("Type the length of the rectangle:\n"))
        rec_hight = float(input("Type the hight of the rectangle:\n"))
        return rec_length * rec_hight
    elif x == "triangle":
        tri_length = float(input("Type the length of side of the triangle:\n"))
        tri_hight = float(input("Type the hight of the triangle:\n"))
        return (tri_length * tri_hight)/2
    else:
        radius = float(input("Type the radius of the circle:\n"))
        ar = (2.0 * 3.14 * radius)
        return float(ar)

print(area())

