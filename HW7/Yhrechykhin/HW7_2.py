import re

print("Hello user, let's create new password!")
print()
print('''At least 1 letter between [a-z] and 
1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
''')

password = input("Please enter the password: ")

if not 5 < len(password) < 17:
    print("Your password invalid, lenght must be between 6 and 16 characters.")
elif len(re.findall('[A-Z]', password)) == 0:
    print("Your password invalid, you need at least 1 letter between [A-Z].")
elif len(re.findall('[a-z]', password)) == 0:
    print("Your password invalid, you need at least 1 letter between [a-z].")
elif len(re.findall('[0-9]', password)) == 0:
    print("Your password invalid, you need at least 1 number between [0-9].")
elif len(re.findall('[$#@]', password)) == 0:
    print("Your password invalid, you need at least 1 symbol from [$#@].")
else:
    print('''Congratulation!!! Your password correct.
Please remember it.''')