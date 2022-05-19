my_list = [3, 5, 7, 9]

#first version
for index in range(len(my_list)):
    my_list[index] = float(my_list[index])

print(f"Result of float operation - {my_list}")

#second version
print(f"Result of float operation - {[float(x) for x in my_list]}")
