import area_of_figures as aof

print('This program calculates the area of a figure if all its sides are found')
ent = input('Enter "r" - if you want to calculate the area of a rectangle\n'
            'Enter "t" - if you want to calculate the area of a triangle\n'
            'Enter "c" - if you want to calculate the area of a circle\n')
if ent.lower() == 'r':
    aof.rectangle_area()
elif ent.lower() == 't':
    aof.triangle_area()
elif ent.lower() == 'c':
    aof.circle_area()
