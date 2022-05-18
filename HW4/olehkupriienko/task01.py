number = input('Enter the number: ')

if not number.isdigit():
    if int(number) < 0:
        print('You entered the wrong number')
else:
    factorial = 1
    for i in range(1, int(number) + 1):
        factorial *= i
    print(f'Factorial of {number} is {factorial}')
