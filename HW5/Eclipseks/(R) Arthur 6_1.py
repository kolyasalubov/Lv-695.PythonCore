lst_div_2 = []
lst_div_3 = []
not_div = []

for item in range(10):
    if item % 2 == 0 and item > 0:
        lst_div_2.append(item)
    elif item % 2 != 0 and item % 3 == 0:
        lst_div_3.append(item)
    elif item % 2 != 0 and item % 3 != 0:
        not_div.append(item)

print(lst_div_2)
print(lst_div_3)
print(not_div)