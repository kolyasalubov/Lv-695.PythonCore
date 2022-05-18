num = input()

first_digit = int(num[0])
second_digit = int(num[1])
third_digit = int(num[2])
fourth_digit = int(num[3])
print(first_digit+second_digit+third_digit+fourth_digit)

print(num[::-1])

list_of_digit = list(num)
sorted_list_of_digit = sorted(list_of_digit)
print(*sorted_list_of_digit, sep='')
