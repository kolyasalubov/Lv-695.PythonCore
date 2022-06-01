even_numbers = []
odd_numbers = []
not_divisible = []


for numbers in range(1,11):
    if numbers % 2 == 0:
        even_numbers.append(numbers)
    elif numbers % 3 == 0:
        odd_numbers.append(numbers)
    elif numbers % 2 != 0 and numbers % 3 != 0:
        not_divisible.append(numbers)

print(f'Even numbers that are divisible by 2 = {even_numbers}')
print(f'Odd numbers, which are divisible by 3 = {odd_numbers}')
print(f'Numbers that are not divisible by 2 and 3 = {not_divisible}')