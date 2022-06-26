from random import randint

count = 0
while True:
    num = randint(1, 101)
    number = int(input("Print the number from 1 to 100:"))
    count += 1
    if number == num:
        print("You won!")
        break
    elif count >= 10:
        print("You lose, game over")
        break
    else:
        print("Try again")
