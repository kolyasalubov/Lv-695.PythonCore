import re

passw = input("Enter the password: ")


if (len(re.findall('[A-Z]', passw)) == 0
    or len(re.findall('[a-z]', passw)) == 0
    or len(re.findall('[$#@]', passw)) == 0
    or len(re.findall('[0-9]', passw)) == 0
    or len(passw) < 6
    or len(passw) > 16):
        print("Not correct try again!")
else:
    print("Password correct!")
    


