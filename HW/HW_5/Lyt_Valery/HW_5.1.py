even_numbers_list = []
odd_numbers_list = []
not_divisible6_list = []

for item in range(1, 11):
    if item % 2 == 0:
        even_numbers_list.append(item)
    elif item % 3 == 0 and item % 2 != 0:
        odd_numbers_list.append(item)
    else:
        not_divisible6_list.append(item)

print(even_numbers_list)
print(odd_numbers_list)
print(not_divisible6_list)
