import re

password = input("Пароль: ")
if len(password) < 6 or len(password) > 16:
    print("Некоректный пароль")
elif len(re.findall('[A-Z]', password)) == 0:
    print("Некоректный пароль")
elif len(re.findall('[a-z]', password)) == 0:
    print("Некоректный пароль")
elif len(re.findall('[0-9]', password)) == 0:
    print("Некоректный пароль")
elif len(re.findall('[$#@]', password)) == 0:
    print("Некоректный пароль")
else:
    print("Правильный пароль")
    