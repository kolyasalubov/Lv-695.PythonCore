import math

number_of_digits = input("Enter your 4-digit number: ")
new_list_of_digits = [int(i) for i in number_of_digits]

print(f"Multiplication of digits = {math.prod(new_list_of_digits)}")

print(f"Reversed digit: {int(number_of_digits[::-1])}")

new_list_of_digits.sort()
convert_list_to_int = int(''.join(map(str, new_list_of_digits)))

print(f"Sorted digits: {convert_list_to_int}")