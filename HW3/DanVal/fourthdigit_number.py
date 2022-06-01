number = input("Input number \n")
while len(number) != 4:
    number = input("Input number with 4 digits\n")

nl = list(map(int, number))
print(f"Product of numbers = {nl[0]*nl[1]*nl[2]*nl[3]}")
print(f"Reverse numbers => {number[::-1]}")
print(f"Sorted numbers => {int(''.join(sorted(number, reverse=True)))}")