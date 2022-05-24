import random

numb_secret = random.randint(1, 100)

numb_user = int(input('Try to guess a number between 1 and 100: '))
while numb_user != numb_secret:
    if numb_user < numb_secret:
        numb_user = int(input('The entered number is less than the secret one. Try again: '))
    # elif numb_user > numb_secret:
    else:
        numb_user = int(input('The entered number is greater than the secret one. Try again: '))
else:
    print(f'Congrats! You have guessed the number. The secret number is {numb_secret}')
