import random

flag = True
x = random.randint(0, 100)

while flag:
    ans = int(input("Choose your number.\n"))
    if ans == x:
        print("You win")
        flag = False
    else:
        print("Your number is too hight. Enter next number." if ans > x else "Your number is too low. Enter next number.")
        
