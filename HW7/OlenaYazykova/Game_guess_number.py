import random

number_1=random.randint(1,100)
print(number_1)
number_2=int(input("Guess a number from 1 to 100: "))
while  number_2!=number_1:
    if number_2<0 or number_2>100:
        number_2=int(input("It's wrong, the number is in the range 1 to 100."))
    elif number_2-number_1>0:
        number_2=int(input(f"Number {number_2} is bigger than hidden number, try once more."))
    elif number_2-number_1<0:
       number_2=int(input(f"Number {number_2} is less than hidden number, try once more."))
else:
    print(f"Excellent! You guessed the number {number_1}.")