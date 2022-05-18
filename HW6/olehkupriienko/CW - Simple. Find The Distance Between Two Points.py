x1, y1 = int(input('Input value for x1: ')), int(input('Input value for y1: '))
x2, y2 = int(input('Input value for x2: ')), int(input('Input value for y2: '))


def distance(x1, y1, x2, y2):
    # return distance between two ordered pairs rounded to two decimal places

    return round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, 3)


print(distance(x1, y1, x2, y2))
