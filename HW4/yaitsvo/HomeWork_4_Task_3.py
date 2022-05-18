f0 = 0
f1 = 1
for i in range(int(input())):
    print(f0, end=' ')
    f0, f1 = f1, f1 + f0

