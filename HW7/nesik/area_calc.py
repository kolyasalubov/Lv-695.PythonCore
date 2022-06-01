PI = 3.14


def AreaOfRectangle():
    width = float(input('Please Enter the Width of a Rectangle: '))
    height = float(input('Please Enter the Height of a Rectangle: '))
    print(f'The area of Rectangle is {width * height}')


def AreaOfTriangle():
    height = float(input('Please Enter the Height of a Triangle: '))
    base = float(input('Please Enter the Base of a Triangle: '))
    print(f'The Area of Triangle is {0.5 * base * height}')


def AreaOfCircle():
    radius = float(input('Please Enter the Radius lenght of a Circle: '))
    print(f'The Area of Circle is {radius ** 2 * PI}')
