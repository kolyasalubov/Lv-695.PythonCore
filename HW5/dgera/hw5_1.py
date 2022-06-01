nums_even_div_2 = []
nums_odd_div_3 = []
nums_other = []

for i in range(1, 11):
    if i%2 == 0:
        nums_even_div_2.append(i)
    elif i%3 == 0:
        nums_odd_div_3.append(i)
    else:
        nums_other.append(i)

print(f'Even numbers that are divisible by 2: {nums_even_div_2}')
print(f'Odd numbers, which are divisible by 3: {nums_odd_div_3}')
print(f'Numbers that are not divisible by 2 and 3: {nums_other}')
