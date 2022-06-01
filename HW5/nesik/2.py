login = input('Enter your login: ')


while login != 'First':
    login = input(
        'You entered the wrong login!\nPlease enter the login again: ')
else:
    print(f'Hello, {login}')
