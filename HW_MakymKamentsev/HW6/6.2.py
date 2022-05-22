"""Task2. Write a program that calculates the area of a rectangle, triangle and circle
(write three functions to calculate the area, and call them in the main program depending on the user's choice).
"""

def rectangle(a,b):
    return a*b
def triangle(a,b):
    return 0.5 * a/b
def circle(r):
    return r**2  * 3.14


print(f"area of a rectangle = {rectangle(1,2)}, triangle = {triangle(3,4)}, circle = {circle(5)}")
triangle(3,4)
circle(5)