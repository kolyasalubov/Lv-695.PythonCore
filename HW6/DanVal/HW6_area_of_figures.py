# I had time and inspiration :)

def validator(*args):

    """
    Validation of data. Must be float or int, bigger than 0.
    Args must not be empty
    """

    if len(args) == 0 or \
        any(map(lambda x: not isinstance(x, (int, float)), args)) or \
        any(map(lambda x: x<0, args)):
        return False
    else:
        return True

# print(f"validator with notdigit => {validator(1,3,'f')}")
# print(f"validator with <0 => {validator(1, -3, 4.6)}")
# print(f"validator with empty args => {validator()}")
# print(f"validator with correct data => {validator(1.4, 5.5, 8)}")

def area_rectangle(*args):
    """
    Function calculates area of rectangle
    If function has one parametr, calculates area of square.
    """
    if not validator(*args) or len(args) > 2:
        return f"Invalid data. It must be 1 or 2 integer or float number, bigger than 0"
    
    match len(args):
        case 1:
            return f"Area of square => {round((args[0])**2, 2)}"
        
        case 2:
            return f"Area of rectangle => {round(args[1]*args[0], 2)}"

# print(f"area_rectangle with invalid data => {area_rectangle(1, 'r')}")
# print(f"area_rectangle with 1 argument => {area_rectangle(4.0)}")
# print(f"area_rectangle with 2 argument => {area_rectangle(4.0, 5)}")


def area_triangle(*args):
    """
    Function calculates area of triangle using Geron's formula
    """

    if not validator(*args) or len(args) != 3:
        return f"Invalid data. It must be 3 integer or float numbers, bigger than 0"
   
    else:
        p = (args[0] + args[1] + args[2])/2
        try: 
            return round((p*(p-args[0])*(p-args[1])*(p-args[2]))**0.5, 2)
        except:
            return f"incorrect lengts of triangles borders"

# print(f"Area triangle with correct data {area_triangle(2, 5, 6)}")
# print(f"Area triangle with incorrect data. Try/except using => {area_triangle(2, 15, 6)}")

def area_circle(*args):
    """
    Function calculates area of circle
    """
    if not validator(*args) or len(args) != 1:
        return f"Incorrect data"
    else:
        return round(args[0]**2*3.14, 2)
    
# print(f"Area of circle with invalid data => {area_circle(1, 3)}")
# print(f"Area of circle with correct data => {area_circle(6)}")

function_dict = {'1': area_rectangle, '2': area_triangle, '3': area_circle}

print("You can starting 3 function:")
print("1 - to calculation area of rectangle. Must has 1 or 2 float args, bigger than 0")
print("2 - to calculation area of triangle. Must has 3 float args, bigger than 0")
print("3 - to calculation area of circle. Must has 1 float args, bigger than 0")
my_func = function_dict[input("input number of function\n")]

try:
    print(my_func(*map(float,input("Input arguments of function with commas between its\n").split(','))))
except:
    print("You input invalid arguments")
