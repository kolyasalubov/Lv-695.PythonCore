import re

password = input('Please enter a password: ')

while True:
    if 6 <= len(password) <= 16 \
            and re.search(r'[a-z]', password) is not None \
            and re.search(r'[A-Z]', password) is not None \
            and re.search(r'[0-9]', password) is not None \
            and re.search(r'[#@$]', password) is not None:
        print()
        print('=== Congrats! Your password is approved! ===')
        break
    else:
        print()
        print('=== Password has to meet the following criteria ===')
        print('At least 1 letter between [a-z] and 1 letter between [A-Z].')
        print('b) At least 1 number between [0-9].')
        print('c) At least 1 character from [$#@].')
        print('d) Minimum length 6 characters.')
        print('e) Maximum length 16 characters.')
        password = input('Try again: ')