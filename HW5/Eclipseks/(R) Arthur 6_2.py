dic_logins = {"aba234": "Qwert123", "Kolpo298": "Popoi"}
enter_login = input("Write correct login: ")

while enter_login in dic_logins.values():
    print("Hello, user =)")
    break
if enter_login not in dic_logins.values():
    print("Login not correct. Pls try again.")