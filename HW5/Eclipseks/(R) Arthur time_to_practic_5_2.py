""" While """

lis_long = []
start = 0
while start < 100:
    start += 1
    if start % 2 == 0:
        continue
    else:
        lis_long.append(start)
print(lis_long)

""" For """

lis_long = []

for item in range(100):
    if item % 2 == 0:
        continue
    else:
        lis_long.append(item)
print(lis_long)