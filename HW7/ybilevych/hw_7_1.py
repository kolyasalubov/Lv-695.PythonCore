import my_math

request = input("The area of which figure needs to be calculated? (rectangle, triangle or circle)\n")
if request.lower() == "rectangle":
    print(my_math.rectangle())
elif request.lower() == "triangle":
    print(my_math.triangle())
elif request.lower() == "circle":
    print(my_math.circle())

