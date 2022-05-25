from calc_areas import rectangle, triangle, circle

choice = input('Please enter the figure: ')

if choice == 'rectangle':
    lens = int(input("Enter length: "))
    widt = int(input("Enter width: "))
    print(f'Rectangle area is {rectangle(lens, widt)}')
elif choice == 'triangle':
    hight = float(input("Enter hight: "))
    side = float(input("Enter side: "))
    print(f'Triangle area is {triangle(hight, side)}')
elif choice == 'circle':
    rad = int(input("Enter radius: "))
    print(f'Circle area is {circle(rad)}')
else:
    print("Not correct figure, try again!")