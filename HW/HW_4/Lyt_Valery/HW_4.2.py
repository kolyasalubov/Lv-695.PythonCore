list_int = []

while len(list_int) < 5:
    list_int.append(int(input()))

print(list_int)

list_float = []
while list_int:
    val = float(list_int[0])
    list_float.append(val)
    del(list_int[0])

print(list_float)
