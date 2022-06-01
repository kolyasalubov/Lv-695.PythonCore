number = int(input("Введите число: "))

a = 0
b = 1
for i in range(2, number+1):
    a, b = b, a + b
    print("Числа Фибоначчи: ", b)

