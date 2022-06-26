print("rectangle = 1 \ntriangle = 2 \ncircle = 3 ")
type_area = int(input("What area do you want to calculate?\n "))


def area_of_rectangle(number_1, number_2):
    area = number_1 * number_2
    return area


def area_of_triangle(number_1, number_2, number_3):
    p = (number_1 + number_2 + number_3) / 2
    area = (p * (p - number_1) * (p - number_2) * (p - number_3)) ** (1/2)
    return area


def area_of_circle(number_1):
    area = 3.14 * (number_1 ** 2)
    return area


if type_area == 1:
    print("Write parameters:")
    print(area_of_rectangle(float(input()), float(input())))
elif type_area == 2:
    print("Write parameters:")
    print(area_of_triangle(float(input()), float(input()), float(input())))
elif type_area == 3:
    print("Write parameters:")
    print(area_of_circle(float(input())))
else:
    print("Oppps, try again")
