import random

user_guess_number = 0
rand_number = random.randint(1, 100)

while user_guess_number != rand_number:
    user_guess_number = int(input("Guess the number from 1 to 100: "))
    if user_guess_number > rand_number:
        print("The number should be smaller!")
    elif user_guess_number < rand_number:
        print("The number should be higher!")
    else:
        print(f"You guessed that number {rand_number}")
        break
