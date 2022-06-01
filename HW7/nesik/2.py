import re

password = input('Enter the password: ').strip()


while True:
    if 6 <= len(password) <= 16 \
            and re.search(r'[]', password) is not None \
            and re.search(r'[]', password) is not None \
            and re.search(r'[]', password) is not None \
            and re.search(r'[]', password) is not None:
        print()
        print('Your password is approved')
    else:
        print('You entered a wrong password')
