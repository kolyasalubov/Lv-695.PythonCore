import module

choose_action = input("1.Calculates the area of triangle\n2.Calculates the area of rectangle\n3.Calculates the area"
                      "of circle\nChoice your action: ")
if choose_action == "1":
    choose_height = float(input("Enter height of triangle: "))
    choose_base = float(input("Enter base of triangle: "))
    print(f"{module.area_of_triangle(choose_height, choose_base)}")
elif choose_action == "2":
    choose_height = float(input("Enter height of rectangle: "))
    choose_base = float(input("Enter base of rectangle: "))
    print(f"Area of rectangle = {module.area_of_rectangle(choose_height, choose_base)}")
elif choose_action == "3":
    choose_radius = float(input("Enter radius of circle: "))
    print(f"Area of circle = {module.area_of_circle(choose_radius)}")
