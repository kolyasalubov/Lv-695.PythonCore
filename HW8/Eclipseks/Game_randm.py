import random

rand_dig = random.randint(1, 100)
user_dig = 0
count_time = []

print("""
Welcome to the game 'Try to guess'
We guessed digital for 1 to 100.
Enter digit!
If u make a mistake we help u.
Lets do it!!!
""")

while user_dig != rand_dig:
    user_dig = int(input("Enter digit: "))
    if user_dig > 100:
        count_time.append(user_dig)
        print("Enter digit for 1 to 100!")        
    elif user_dig > rand_dig:
        count_time.append(user_dig)
        print('Oups our digit is less than u. Try again)')
    elif user_dig < rand_dig:
        count_time.append(user_dig)
        print('Oups our digit is more than u. Try again)')

count_try = len(count_time)
print(f"Congratulations you guess right on the {count_try}th try!!!")