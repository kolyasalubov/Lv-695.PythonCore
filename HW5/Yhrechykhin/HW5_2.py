login = input('Please enter your login: ')

while login != 'First':
    login = input('Error message: wrong login\nPlease enter your login: ')
else:
    print(f'Welcome, {login}!')