import random

number = random.randint(1, 101)

print('Welcome to number guessing game')

def is_valid(num):
    """The function of checking the entered data for correctness"""
    if num.isdigit():
        num = int(num)
        if 1 <= num <= 100:
            return True
        else:
            return False
    else:
        return False


while True:
    response = input('Enter a number from 1 to 100:')
    if not is_valid(response):
        print('Or maybe we can still enter an integer from 1 to 100?')
        continue
    val = int(response)

    if val < number:
        print('Your number is less than expected, please try again')
    elif val > number:
        print('Your number is higher than expected, please try again')
    else:
        print('You guessed it, congratulations!')
        break

print('Thanks for playing the number guessing game.')
