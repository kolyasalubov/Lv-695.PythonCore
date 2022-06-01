number_of_fuc = int(input("Write numer: "))
count = 1

for item in range(number_of_fuc):
        item += 1
        count *= item
print(f"{number_of_fuc}! = ", count)