from my_math import area_circle as ac
from my_math import area_rectangle as ar
from my_math import area_triangle as at

function_dict = {'1': ac, '2': ar, '3': at}

my_func = function_dict[input("input number of function\n1 - area of circle\n2 - area of rectangle\n3 - area of triangle\n")]

try:
    print(my_func(*map(float,input("Input arguments of function with commas between its\n").split(','))))
except:
    print("You input invalid arguments")

