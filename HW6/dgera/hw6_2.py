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
    
    print('\n=== Data for calculation ===')
    radius = float(input('Please enter a length of the radius (in centimeters): '))
    
    print('\n========== Result ==========')
    print(f'Circle area is {3.14*radius**2} centimeters')


print('''Press "R" button - to calculate rectangle area.
Press "T" button - to calculate triangle area.
Press "C" button - to calculate circle area.
Press "E" button - to exit.''')
user_choice = input('Please choice what do you want to calculate: ').upper()

while user_choice not in ('R', 'T', 'C', 'E'):
    print('\n======== Attention =========')
    print('Only "R", "T", "C" and "E" buttons are allowed.')
    user_choice = input('Please press a button again: ').upper()

match user_choice:
    case 'R':
        area_rectangle()
    case 'T':
        area_triangle()
    case 'C':
        area_circle()
    case 'E':
        print('\nOk. See you later ;)')
