import re

password = input("Enter the password: ")
# password = "2aZ!ddd"   #incorrect
# password = "rd@D21"    #correct 
my_set = {'[A-Z]', '[a-z]', '[$#@]', '[0-9]'}

if not all(re.findall(x, password) for x in my_set) or not  5 < len(password) < 17:
    print("Incorrect password")
else:
    print("Password correct!")
