number_1 = 0
number_2 = 1
item = 0

while item < 20:
    item = number_1 + number_2
    print("item", item)
    number_2 = number_1
    print("number_2", number_2)
    number_1 = item
    print("number_1", number_1)

print(item)
