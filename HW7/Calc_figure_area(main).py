from figure_area_calculation import *


print('Hello!\nI will help you to calculate the area of figure you need.')


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
