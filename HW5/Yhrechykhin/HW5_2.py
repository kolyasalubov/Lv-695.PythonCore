login = input('Please enter your login: ')

data_list = {}

data_list['login'] = login

while True:
    if data_list['login'] == 'First':
        print('Welcome user!!!')
        break
    else:
        print('Error message: try again')
        break

    