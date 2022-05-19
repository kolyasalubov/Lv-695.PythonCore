
key=True
def is_digit(c,key):
    """This function check if the input parameter is integer or float number"""

    if c.isdigit():
        c=int(c)
        key=False
        return c,key
    else:
        try:
            float(c)
            c=float(c)
            key=False
            return c,key
        except ValueError:
            key=True
            return c,key
while key==True:
    c=input("Enter the value of a: ")
    is_digit(c,key)
    a,key=is_digit(c,key)
    if key==True:
        print("The variable is not a number!")
key=True
while key==True:
    c=input("Enter the value of b: ")
    is_digit(c,key)
    b,key=is_digit(c,key)
    if key==True:
        print("The variable is not a number!")
print(f"a+b = {a+b}")
print(f"a-b = {a-b}")
print(f"a*b = {a*b}")
print(f"a**b = {a**b}")
try:
    print(f"a/b = {a/b}")
    print(f"a//b = {a//b}")
except ZeroDivisionError:
    print("Division by 0!")