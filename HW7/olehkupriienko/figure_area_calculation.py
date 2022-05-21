
def calculate_rectangle_area():
    length = input('Please, enter the value of rectangle length! Length = ')
    while True:
        if length.isdigit():
            if float(length) > 0:
                length = float(length)
                print(f'Ok! Length = {length}')
                break
        length = input('Ops! Something went wrong!\nPlease, enter the value of the rectangle length! Length = ')

    width = input('Please, enter the value of rectangle width! Width = ')
    while True:
        if width.isdigit():
            if float(width) > 0:
                width = float(width)
                print(f'Ok! Width = {width}')
                break
        width = input('Ops! Something went wrong!\nPlease, enter the value of the rectangle width! Width = ')

    rectangle_area = round(length * width, 2)
    return rectangle_area


def calculate_triangle_area():
    a = input('Please, enter the value of the side length! a = ')
    while True:
        if a.isdigit():
            if float(a) > 0:
                a = float(a)
                print(f'Ok! a = {a}')
                break
        a = input('Ops! Something went wrong!\nPlease, enter the value of first side length! a = ')

    h = input('Please, enter the value of the height! h = ')
    while True:
        if h.isdigit():
            if float(h) > 0:
                h = float(h)
                print(f'Ok! h = {h}')
                break
        h = input('Ops! Something went wrong!\nPlease, enter the value of second side length! b = ')

    triangle_area = round((0.5 * a * h), 2)
    return triangle_area


def calculate_circle_area():
    from math import pi, pow
    r = input('Please, enter the value of circle radius! r = ')
    while True:
        if r.isdigit():
            if float(r) > 0:
                r = float(r)
                print(f'Ok! r = {r}')
                break
        r = input('Ops! Something went wrong!\nPlease, enter the value of circle radius! r = ')
    circle_area = round(pi * pow(r, 2), 2)
    return circle_area
