number = int(input("Input number\n"))
factorial = 1

for i in range(2, number + 1):
    factorial *= i

print(f"Factorial of {number} = {factorial}")
