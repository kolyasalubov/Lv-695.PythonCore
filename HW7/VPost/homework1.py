import homework_2

request = input("The area of which figure needs to be calculated?\n")

if request == 1:
    lens = int(input("Enter length: "))
    widt = int(input("Enter width: "))
    print(homework_2.rectangle(lens, widt))
elif request == 2:
    higt = int(input("Enter hight: "))
    side = int(input("Enter side: "))
    print(homework_2.triangle(higt, side))
elif request == 3:
    rad = int(input("Enter radius: "))
    print(homework_2.circle(rad))
else:
    print("Not correct, try again!")
