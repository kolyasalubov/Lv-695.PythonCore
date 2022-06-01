# Find factorial of a number
number = int(input('Enter the number: ').strip())

factorial = 1

for i in range(1, number+1):
    factorial = factorial * i

print(f'The factorial {number} is: {factorial}')
