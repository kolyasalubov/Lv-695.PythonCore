import random

def hangman():
    print("Привет! Добро пожаловать в игру Виселица")

    list = ['red', 'blue', 'yellow', 'green', 'white', 'black', 'brown', 'orange', 'pink']

    secret = random.choice(list)
    guesses = 'euoia'
    turns = 5

    while turns > 0:
        missed = 0
        for letter in secret:
            if letter in guesses:
                print(letter, end='')
            else:
                print('_', end='')
                missed += 1
        if missed == 0:
            print("\nТы выиграл!")
            break
        guess = str(input("\nВведите букву: "))
        guesses += guess

        if guess not in secret:
            turns -= 1
            print("\nВы не угадали")
            print('\n', "Осталось попыток: ", turns)
            if turns < 5: print('\n | ')
            if turns < 4: print(' O ')
            if turns < 3: print('/|\ ')
            if turns < 2: print(' | ')
            if turns < 1: print('/ \ ')
            if turns == 0: print("Это слово: ", secret)
answer = "yes"
while answer == "yes":
    hangman()
    print("Хочешь сыграть снова? (yes)")
    answer = str(input("Ваш ответ:"))



