import math


side_1 = int(input("Введите значение первой стороны треугольника:"))
side_2 = int(input("Введите значение второй стороны треугольника:"))
side_3 = int(input("Введите значение третьей стороны треугольника:"))
radius = int(input("Введите радиус круга:"))
FirstSide = int(input("Введите значение висоты прямоугольника:"))
SecondSide = int(input("Введите значение ширины прямоугольника:"))


def area_thriangle (side_1, side_2, side_3):
    p = (side_1 + side_2 + side_3) / 2
    S = math.sqrt(p * (p - side_1) * (p - side_2) * (p - side_3))
    return print("Площадь треугольника:", S)


print(area_thriangle (side_1, side_2, side_3))


def area_circle (radius):
    S = math.pi * (radius ** 2)
    return print("Площадь круга:", S)


print(area_circle (radius))


def area_rectangle (FirstSide, SecondSide):
    S = FirstSide * SecondSide
    return print("Площадь прямоугольника:", S)


print(area_rectangle (FirstSide, SecondSide))


