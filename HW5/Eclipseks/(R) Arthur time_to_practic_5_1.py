""" While """

lis_fis = []
x = 0
while x < 100:
    x += 1
    if x % 2 != 0:
        continue
    else:
        lis_fis.append(x)
print(lis_fis)

""" For """
lis_fis = []
for item in range(100):
    if item % 2 != 0 or item == 0:
        continue
    else:
        lis_fis.append(item)
print(lis_fis)
