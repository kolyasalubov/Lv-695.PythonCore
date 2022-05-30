import random

number = random.randint(1, 100)

number = int(input('Put number between 1 and 100: '))
while number != number:
    if number < number:
        number = int(input('The number is less than first number: '))
    else:
        number = int(input('The number is bigger than first number: '))
else:
    print(f'{number}\nYou win ')