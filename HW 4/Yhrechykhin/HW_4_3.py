# with while loop
num = int(input('Enter the number: '))
f1, f2 = 0, 1

while f1 < num:
    if num == 1:
        print('1')
        break
    else:
         print(f1, end=' ')
         f1, f2 = f2, f1 + f2

# with for loop:
n = int(input('Enter the number: '))
x1, x2 = 0, 1

for i in range(n):
    print(x1, end=' ')
    x1, x2 = x2, x1 + x2
