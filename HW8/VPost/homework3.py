import random

number = random.randint(1, 101)
print(number)

your_choice = int(input("Input your number\n"))

while number != your_choice:
    if number > your_choice:
        print("your number less that mine")
    else :
        print("your number bigger that mine")
    your_choice = int(input("Try again! Input your number\n"))

print("You are win")