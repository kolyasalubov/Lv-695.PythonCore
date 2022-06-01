even_div_by_2 = []
odd_div_by_3 = []
num_not_div_by_2_and_3 = []

for _ in range(1, 11):
    if _ % 2 == 0:
        even_div_by_2.append(_)
    if _ % 2 != 0 and _ % 3 == 0:
        odd_div_by_3.append(_)
    if _ % 2 != 0 and _ % 3 != 0:
        num_not_div_by_2_and_3.append(_)

print('Even numbers from 1 to 10 divisible by 2 are:', even_div_by_2)
print('Odd numbers from 1 to 10 divisible by 3 are:', odd_div_by_3)
print('Numbers from 1 to 10 not divisible by 2 and 3 are:', num_not_div_by_2_and_3)
