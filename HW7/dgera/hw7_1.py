import area_calculator

print('Press "R" button - to calculate rectangle area.')
print('Press "T" button - to calculate triangle area.') 
print('Press "C" button - to calculate circle area.') 
print('Press "E" button - to exit.')
user_choice = input('Please choice what do you want to calculate: ').upper()

while user_choice not in ('R', 'T', 'C', 'E'):
    print('\n======== Attention =========')
    print('Only "R", "T", "C" and "E" buttons are allowed.')
    user_choice = input('Please press a button again: ').upper()

match user_choice:
    case 'R':
        area_calculator.area_rectangle()
    case 'T':
        area_calculator.area_triangle()
    case 'C':
        area_calculator.area_circle()
    case 'E':
        print('\nOk. See you later ;)')
