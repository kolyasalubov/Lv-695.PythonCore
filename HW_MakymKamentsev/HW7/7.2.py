import re

password = input("Password:\n")
if len(password) < 6 or len(password) > 16:
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
    print("Your password correct.")
    
