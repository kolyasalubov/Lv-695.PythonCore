import re

while True:
    password = input("print your password\n")

    result = re.findall('[a-z]', password)
    result1 = re.findall("\d", password)
    result2 = re.findall("\\$|#|@", password)
    result3 = re.findall('[A-Z]', password)
    if not 6 <= len(password) <= 16:
        print("Minimum length 6 characters and maximum length 16 characters")
    elif not result:
        print("You need to use a-z")
    elif not result3:
        print("You need to use A-Z")
    elif not result1:
        print("You need to use numbers")
    elif not result2:
        print("You need to use # or $ or @")
    else:
        print(f"Your password is: {password}")
        break
