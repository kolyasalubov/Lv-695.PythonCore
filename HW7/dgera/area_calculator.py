def area_rectangle() -> None:
    """Print a rectangle area calculation"""

    print('\n=== Data for calculation ===')
    side_1 = float(input('Please enter a length of the 1st side (in centimeters): '))
    side_2 = float(input('Please enter a length of the 2nd side (in centimeters): '))
    
    print('\n========== Result ==========')
    print(f'Rectangle area is {side_1*side_2} centimeters')


def area_triangle() -> None:
    """Print a triangle area calculation"""

    print('\n=== Data for calculation ===')
    base_side = float(input('Please enter a length of the base side (in centimeters): '))
    height = float(input('Please enter a length of the height (in centimeters): '))
    
    print('\n========== Result ==========')
    print(f'Triangle area is {base_side*height/2} centimeters')


def area_circle() -> None:
    """Print a circle area calculation"""
    
    import math

    print('\n=== Data for calculation ===')
    radius = float(input('Please enter a length of the radius (in centimeters): '))
    
    print('\n========== Result ==========')
    print(f'Circle area is {math.pi*math.pow(radius, 2)} centimeters')