import re

password = input('''You need to create a strong password!
Requirements:
- at least 1 letter between [a-z] and 1 letter between [A-Z]
- at least 1 number between [0-9]
- at least 1 character from [$#@]
- minimum length 6 characters
- maximum length 16 characters
Please, enter your password: ''')

while True:
    flag1 = len(re.findall("[A-Z]", password)) >= 1  # count_upper_letter at least 1
    flag2 = len(re.findall("[a-z]", password)) >= 1  # count_lower_letter at least 1
    flag3 = len([_ for _ in password if _ in "$#@"]) >= 1  # count_spec_symbol at leat 1
    flag4 = (6 <= len(password) <= 16)  # length must be 6-16
    if flag1 and flag2 and flag3 and flag4:
        print('Great password!')
        break
    else:
        password = input("Your password doesn't meet the requirements\nPlease, choose your password again: ")
