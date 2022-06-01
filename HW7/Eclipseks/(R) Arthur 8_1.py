import Eigth_11

print ("""Choose figure:
[1] Area rectangle
[2] Area triangle
[3] Area circle""")

choose = int(input("Num: "))

if choose == 1:
    lens = int(input("Enter length: "))
    widt = int(input("Enter width: "))
    print(Eigth_11.rectangle(lens, widt))
elif choose == 2:
    higt = int(input("Enter hight: "))
    side = int(input("Enter side: "))
    print(Eigth_11.triangle(higt, side))
elif choose == 3:
    rad = int(input("Enter radius: "))
    print(Eigth_11.circle(rad))
else:
    print("Not correct, try again!")
 
