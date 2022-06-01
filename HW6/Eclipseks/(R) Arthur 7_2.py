import math

print("""
Choose what calculates:
[1] Rectangle
[2] Triangle
[3] Circle
""")

inter_value = (input())
while 1 > 0:
    if inter_value == 1:
        leng = float(input("Write length: "))
        widt = float(input("Write width: "))
        def s_area_rec(length, width):
            area = length * width
            return area
        print(f"Area of a rectangle is: {s_area_rec(leng, widt)}")
    elif inter_value == 2:
        bas = float(input("Write basis: "))
        heig = float(input("Write height: "))
        def s_area_tri(basis, hight):
            area_1 = basis / 2 * hight
            return area_1
        print(f"Area of a triangle is: {s_area_tri(bas, heig)}")
    elif inter_value == 3:
        rad = float(input("Write radius: "))
        def s_area_cic(radi):
            area_2 = math.pi * rad ** 2
            return area_2
        print(s_area_cic(rad))
    else:
        print("Not correct. 'Press enter' and try againe!")
    input()