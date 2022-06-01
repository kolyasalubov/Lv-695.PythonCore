import re


while True:

    user_input = input("Enter a password : ")

    if len(user_input) < 6 or len(user_input) > 16:
        print("Not valid ! Total characters should be between 6 and 16")
        continue
    elif not re.search("[A-Z]", user_input):
        print("Not valid ! It should contain one letter between [A-Z]")
        continue
    elif not re.search("[a-z]", user_input):
        print("Not valid ! It should contain one letter between [a-z]")
        continue
    elif not re.search("[1-9]", user_input):
        print("Not valid ! It should contain one letter between [1-9]")
        continue
    elif not re.search("[~!@#$%^&*]", user_input):
        print("Not valid ! It should contain at least one letter in [~!@#$%^&*]")
        continue
    elif re.search("[\t]", user_input):
        print("Not valid ! It should not contain any space")
        continue
    else:
        print("Password is valid")
        break
