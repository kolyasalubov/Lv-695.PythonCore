# Fibonacci Series using For Loop
fib1 = 1
fib2 = 0

number = int(input('Enter number for Fibonacci Series: ').strip())

for i in range(2, number):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')
