def area_of_triangle(height, base):
    area = 0.5 * height * base
    return area


def area_of_rectangle(height, width):
    area = height * width
    return area


def area_of_circle(radius):
    area = 3.14 * radius ** 2
    return area


print("Choice your action:")
choose_action = int(input("1.Calculates the area of triangle\n2.Calculates the area of rectangle\n3.Calculates the area"
                          "of circle\n"))
if choose_action == 1:
    choose_height = float(input("Enter height of triangle: "))
    choose_base = float(input("Enter base of triangle: "))
    print(f"{area_of_triangle(choose_height, choose_base)}")
elif choose_action == 2:
    choose_height = float(input("Enter height of rectangle: "))
    choose_base = float(input("Enter base of rectangle: "))
    print(f"Area of rectangle = {area_of_rectangle(choose_height, choose_base)}")
elif choose_action == 3:
    choose_radius = float(input("Enter radius of circle: "))
    print(f"Area of circle = {area_of_circle(choose_radius)}")
