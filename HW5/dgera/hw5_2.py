login = input('Please enter your login: ')
while login != 'First':
    login = input('Sorry, the entered login is not exist. Try one more time: ')
else:
    print('===== Success =====')
    print(f'Hello, {login}! It is nice to know that you remember your login. Have a nice day!')