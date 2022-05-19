def area ( name ):
    
 if name == "rectangle":
    a = int(input("Enter rectangle's length: "))
    b = int(input("Enter rectangle's breadth: "))
    area1 = a * b
    print(f"The area of rectangle:", area1)
   
 elif name == ("triangle"):
    h = int(input("Enter triangle's height length: "))
    b = int(input("Enter triangle's base length: "))
    area2 = 0.5 * b * h
    print(f"The area of triangle:", area2)

 elif name == ("circle"):
    r = int(input("Enter circle's radius length: "))
    pi = 3.14
    area3 = pi * r **2
    print(f"The area of circle:", area3)

if __name__ == "__main__" :   
      print("Calculate Shape Area")
shape_name = input("Enter the name of shape whose area you want to find: ")
area(shape_name)