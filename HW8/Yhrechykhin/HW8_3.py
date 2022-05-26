import random                    

number = random.randint(1, 101)  

print('Welcome to the number guessing game')

def is_valid(num):
    if num.isdigit():
        num = int(num)
        if 1 <= num <= 100:
            return True
        else:
            return False
    else:
        return False
        
while True:
    val = input('Please enter a number between 1 and 100:')
    if not is_valid(val):
        print('Maybe we can still enter an integer from 1 to 100?')
        continue
    val = int(val)
    
    if val < number:
        print('Your number is less than what you have guessed, please try again')
    elif val > number:
        print('Your number is higher than expected, please try again')
    else:
        print('You guessed it, congratulations!')
        break

print('Thanks for playing the number guessing game. See you...')
