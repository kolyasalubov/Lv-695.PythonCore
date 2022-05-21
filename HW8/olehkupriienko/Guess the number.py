from random import *
n = randint(1, 100)
print('Hello!\nGuess the number from 1 to 100!')


def is_valid(num):
    return num.isdigit() and 1 <= int(num) <= 100


def is_valid_num():
    while True:
        print('Input your number:')
        num = input()
        if is_valid(num):
            return int(num)
        else:
            print('Wrong number!')


def compare():
    while True:
        num = is_valid_num()
        if n == num:
            print('Congratulations! You guessed the number!')
            break
        elif n > num:
            print('Your number is less than expected, please try again')
        else:
            print('Your number is higher than expected, please try again')


compare()
