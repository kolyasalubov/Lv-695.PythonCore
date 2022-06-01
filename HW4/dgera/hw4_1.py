number = input('Please enter a natural number: ')

if number.isdecimal():
    number = int(number)
    
    for i in range(number+1):
        factorial = 1 if i == 0 else factorial*i
    
    print()
    print(f'The factorial of the entered number is {factorial}')
else:
    print()
    print('Oops! The entered value is not a natural number.')
    print('Please launch this code again.')
    