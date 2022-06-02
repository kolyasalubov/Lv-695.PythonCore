import random

number_1=random.randint(1,100)
number_2=int(input("Guess a number from 1 to 100: "))
count_attempts=1
while  True:
    if number_2==number_1:
        print(f"Excellent! You guessed the number {number_1}. Number of your attempts is {count_attempts}.")
        break
    elif number_2<number_1:
        number_2=int(input("Choose a larger number:"))
        count_attempts+=1
    else:
        number_2=int(input("Choose a smaller number: "))
        count_attempts+=1
