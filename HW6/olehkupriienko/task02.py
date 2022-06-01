print('Hello!\nI will help you to calculate the area of figure you need.')


def calculate_rectangle_area():
    length = input('Please, enter the value of rectangle length! Length = ')
    while True:
        if length.isdigit():
            if float(length) > 0:
                length = float(length)
                print(f'Ok! Length = {length}')
                break
        length = input('Ops! Something went wrong!\nPlease, enter the value of rectangle length! Length = ')

    width = input('Please, enter the value of rectangle width! Width = ')
    while True:
        if width.isdigit():
            if float(width) > 0:
                width = float(width)
                print(f'Ok! Width = {width}')
                break
        width = input('Ops! Something went wrong!\nPlease, enter the value of rectangle Width! Width = ')

    rectangle_area = round(length * width, 2)
    return rectangle_area


def calculate_triangle_area():
    while True:
        a = input('Please, enter the value of first side length! a = ')
        while True:
            if a.isdigit():
                if float(a) > 0:
                    a = float(a)
                    print(f'Ok! a = {a}')
                    break
            a = input('Ops! Something went wrong!\nPlease, enter the value of first side length! a = ')

        b = input('Please, enter the value of second side length! b = ')
        while True:
            if b.isdigit():
                if float(b) > 0:
                    b = float(b)
                    print(f'Ok! b = {b}')
                    break
            b = input('Ops! Something went wrong!\nPlease, enter the value of second side length! b = ')

        c = input('Please, enter the value of first side length! c = ')
        while True:
            if c.isdigit():
                if float(c) > 0:
                    c = float(c)
                    print(f'Ok! c = {c}')
                    break
            b = input('Ops! Something went wrong!\nPlease, enter the value of third side length! c = ')
        if a + b > c and b + c > a and c + a > b:
            p = (a + b + c) / 2
            triangle_area = round((p * (p - a) * (p - b) * (p - c)) ** 0.5, 2)
            break
        else:
            print('The triangle with such sides does not exist. Please enter values of sides again')
    return triangle_area


def calculate_circle_area():
    r = input('Please, enter the value of circle radius! r = ')
    while True:
        if r.isdigit():
            if float(r) > 0:
                r = float(r)
                print(f'Ok! r = {r}')
                break
        r = input('Ops! Something went wrong!\nPlease, enter the value of circle radius! r = ')
    circle_area = round(3.14159265359 * r**2, 2)
    return circle_area


def area_figure():
    available_figure = ('rectangle', 'triangle', 'circle')
    figure = input('Please, enter name one of the figures: rectangle, triangle, or circle?\n').lower()
    while figure not in available_figure:
        figure = input('Sorry, wrong figure!\nEnter name one of the figures: rectangle, triangle, or circle?\n')
    else:
        print(f'Good. Your figure is a {figure}')
    if figure == 'rectangle':
        return f'The area of the {figure} is {calculate_rectangle_area()}'
    elif figure == 'triangle':
        return f'The area of the {figure} is {calculate_triangle_area()}'
    elif figure == 'circle':
        return f'The area of the {figure} is {calculate_circle_area()}'


print(area_figure())
