import random

secret_num = random.randint(1, 100)
user_num = int(input('Guess a number between 1 - 100: ').strip())

while user_num != secret_num:
    if user_num > secret_num:
        user_num = int(input(
            'The entered number is greater than the secret. Enter again: ').strip())
    else:
        user_num = int(input(
            'The entered number is less than the secret. Enter again: ').strip())
else:
    print(
        f'Yee! You guessed the number. The secret number was {secret_num}')
