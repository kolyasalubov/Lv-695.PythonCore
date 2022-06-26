import my_module as mm

print("rectangle = 1 \ntriangle = 2 \ncircle = 3 ")
type_area = int(input("What area do you want to calculate?\n "))

if type_area == 1:
    print("Write parameters:")
    print(mm.area_of_rectangle(float(input()), float(input())))
elif type_area == 2:
    print("Write parameters:")
    print(mm.area_of_triangle(float(input()), float(input()), float(input())))
elif type_area == 3:
    print("Write parameters:")
    print(mm.area_of_circle(float(input())))
else:
    print("Oppps, try again")