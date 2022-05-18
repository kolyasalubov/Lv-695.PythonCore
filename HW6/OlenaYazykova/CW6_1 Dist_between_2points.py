x1=float(input("Enter the value of x1:"))
y1=float(input("Enter the value of y1:"))
x2=float(input("Enter the value of x2:"))
y2=float(input("Enter the value of y2:"))
def distance(x1, y1, x2, y2):
    import math
    return round(math.sqrt((x1-x2)**2+(y1-y2)**2),2)
print(f"The distance between two points is {distance(x1, y1, x2, y2)}.")