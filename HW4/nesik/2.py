# Convert list elements int type -> float type
int_list = [1, 2, 3, 4, 5]
float_list = []

for num in int_list:
    float_list.append(float(num))

print(float_list, type(float_list[0]))
